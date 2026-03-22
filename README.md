InstaPay DevSecOps Project
InstaPay is a secure, demo-ready payment system built for university-level DevSecOps and security modules. This project demonstrates best practices in secure development, CI/CD automation, security scanning, and containerized deployment.
DevSecOps Workflow Diagram
[Code Commit] --> [GitHub Actions CI/CD] --> [SAST: Bandit]
                                   --> [SCA: pip-audit]
                                   --> [Tests: pytest]
                                   --> [Docker Build]
                                   --> [Deployment / Monitoring]
Features
Backend: Flask (Python) with JWT-based authentication
Database: MongoDB for secure transaction storage
Monitoring: Prometheus for real-time metrics and observability
Security:
Non-root Docker user for container safety
Static Application Security Testing (SAST) via Bandit
Software Composition Analysis (SCA) via pip-audit
Continuous Integration / Continuous Deployment (CI/CD) with GitHub Actions
Infrastructure & Deployment:
Docker Compose for local deployment
Kubernetes manifests (demo-ready)
Terraform scripts (demo-ready)
Prerequisites
Docker and Docker Compose installed locally
Optional: Kubernetes and Terraform for infrastructure demos
Quick Start (Run Locally)
Start the full system with:
docker compose up --build
Once up, the following services are available:
Health Check: http://localhost:5000/health
Metrics (Prometheus format): http://localhost:5000/metrics
Prometheus Dashboard: http://localhost:9090
API Endpoints
1. Login (Get JWT)
POST /login
{
  "username": "admin",
  "password": "password"
}
Response: JWT token for authentication.
2. Make a Payment (Protected)
POST /pay
Headers: Authorization: Bearer <token>
{
  "amount": 100,
  "recipient": "bob"
}
Response: Transaction confirmation.
Security Pipeline (CI/CD)
The project includes a GitHub Actions workflow in .github/workflows/ci.yml:
SCA (Dependency Scan): Detects known vulnerabilities using pip-audit.
SAST (Static Analysis): Scans Python code for security flaws with Bandit.
Tests: Runs functional tests using pytest.
Docker Build: Verifies containerization works properly.
All pushes to main automatically trigger this pipeline, ensuring security and reliability.
Project Structure
backend/      # Flask application, Dockerfile, requirements
monitoring/   # Prometheus configuration
k8s/          # Kubernetes deployment manifests (demo)
terraform/    # Sample infrastructure scripts (demo)
.github/      # CI/CD pipeline workflows
Highlights
Fully automated DevSecOps workflow with SAST, SCA, testing, and build verification
Secure containerized application with non-root execution
Easily extensible for real-world CI/CD and security practices
