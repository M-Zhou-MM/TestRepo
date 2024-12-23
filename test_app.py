import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Welcome to the Flask app!"

def test_login_success(client):
    """Test login with correct credentials."""
    response = client.post("/login", json={"username": "admin", "password": "password"})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Login successful!"}

def test_login_failure(client):
    """Test login with incorrect credentials."""
    response = client.post("/login", json={"username": "user", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.get_json() == {"message": "Invalid credentials"}
