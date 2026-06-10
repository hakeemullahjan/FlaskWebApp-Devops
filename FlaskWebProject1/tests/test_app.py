
import pytest
from datetime import datetime
from FlaskWebProject1 import app
import FlaskWebProject1.views as views

@pytest.fixture
def client():
    """Set up the Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home Page' in response.data  # Check if the title exists
    assert str(datetime.now().year).encode() in response.data  # Check the year

def test_home_route_alias(client):
    """Test the /home route."""
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Home Page' in response.data  # Check if the title exists
    assert str(datetime.now().year).encode() in response.data  # Check the year

def test_contact_route(client):
    """Test the contact route."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact' in response.data  # Check if the title exists
    assert b'Your contact page.' in response.data  # Check the message
    assert str(datetime.now().year).encode() in response.data  # Check the year

def test_nonexistent_route(client):
    """Test a nonexistent route."""
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_timestamp_route(client, monkeypatch):
    """Test the timestamp route using a mocked MySQL timestamp."""
    monkeypatch.setattr(views, 'get_mysql_server_timestamp', lambda: '2026-06-01 13:22:00')
    response = client.get('/timestamp')
    assert response.status_code == 200
    assert b'Timestamp' in response.data
    assert b'new response' in response.data
    assert b'2026-06-01 13:22:00' in response.data
