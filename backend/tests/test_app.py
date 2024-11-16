import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app import app

import pytest
# from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_classify_endpoint_with_url(client):
    response = client.post('/classify', json={'url': "https://en.wikipedia.org/wiki/Artificial_intelligence"})
    assert response.status_code == 200
    assert "questions" in response.json
    assert "options" in response.json

def test_classify_endpoint_without_url(client):
    response = client.post('/classify', json={})
    assert response.status_code == 400
    assert response.json['error'] == "URL is required"
