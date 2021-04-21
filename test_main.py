from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello world'}

def test_repository():
    response = client.get('/repository')
    assert response.status_code == 400
    response = client.get('/repository?username=BurnedOlieTree')
    assert response.status_code == 404
    response = client.get('/repository?username=BurnedOliveTree')
    assert response.status_code == 200