import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health(client):
    """Test the health endpoint."""
    # Note: This might fail if MongoDB is not running, 
    # but we can mock it or just check for 200 if it's simple enough.
    # For demo purposes, we just check status code.
    rv = client.get('/health')
    assert rv.status_code == 200
