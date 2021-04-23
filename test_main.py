from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root_no_args():
    response = client.get('/')
    assert response.status_code == 400

def test_root_invalid_args():
    response = client.get('/?username=BurnedOlieTree')
    assert response.status_code == 404
    assert 'Please enter a valid GitHub username' in response.text

def test_root_correct_args():
    response = client.get('/?username=BurnedOliveTree')
    assert response.status_code == 200
    assert '<li>' in response.text