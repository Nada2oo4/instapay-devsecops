from flask import Flask, jsonify, request
import time
import os
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

# --- SECURITY CONFIGURATION ---
# In a real production app, use environment variables and secrets managers.
# JWT (JSON Web Token) is used for stateless authentication.
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key') 
jwt = JWTManager(app)

# --- DATABASE CONNECTION ---
# Connect to MongoDB container using the service name from docker-compose.
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongodb:27017/instapay')
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
db = client.get_database()

# --- MONITORING (Prometheus) ---
# Define metrics to be scraped by Prometheus.
# Counter: track total request count.
# Histogram: track request latency.
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'HTTP Request Latency', ['method', 'endpoint'])

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request(response):
    if hasattr(request, 'start_time'):
        latency = time.time() - request.start_time
        REQUEST_LATENCY.labels(method=request.method, endpoint=request.path).observe(latency)
        REQUEST_COUNT.labels(method=request.method, endpoint=request.path, http_status=response.status_code).inc()
    return response

# --- API ROUTES ---

@app.route('/health')
def health():
    """Health check endpoint to verify API and DB connectivity."""
    db_status = "disconnected"
    try:
        # The ping command is cheap and checks if the server is available.
        client.admin.command('ping')
        db_status = "connected"
    except ConnectionFailure:
        db_status = "disconnected"
    
    return jsonify({
        "status": "healthy",
        "database": db_status,
        "timestamp": time.time()
    }), 200

@app.route('/login', methods=['POST'])
def login():
    """Demo login route returning a JWT token."""
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    # SIMPLE AUTH FOR DEMO: In production, verify against hashed password in DB.
    if username == "admin" and password == "password": # nosec B105
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/pay', methods=['POST'])
@jwt_required()
def pay():
    """Protected payment endpoint. Requires a valid JWT."""
    current_user = get_jwt_identity()
    data = request.json
    amount = data.get('amount')
    recipient = data.get('recipient')
    
    if not amount or not recipient:
        return jsonify({"msg": "Missing amount or recipient"}), 400
    
    transaction = {
        "user": current_user,
        "amount": amount,
        "recipient": recipient,
        "timestamp": time.time()
    }
    db.transactions.insert_one(transaction)
    
    return jsonify({
        "msg": "Payment successful",
        "transaction_id": str(transaction['_id'])
    }), 201

# --- PROMETHEUS METRICS EXPORTER ---
# Expose /metrics endpoint using the prometheus-client WSGI app.
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    # Run the app on all interfaces within the container.
    app.run(host='0.0.0.0', port=5000) # nosec B104
