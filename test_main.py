from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root_no_args():
    response = client.get('/')
    assert response.status_code == 200

def test_root_empty_args():
    response = client.get('/?username=')
    assert response.status_code == 204

def test_root_invalid_args():
    response = client.get('/?username=BurnedOlieTree')
    assert response.status_code == 404
    assert 'Please enter a valid GitHub username' in response.text

def test_root_correct_args():
    response = client.get('/?username=BurnedOliveTree')
    assert response.status_code == 200
    assert '<li>' in response.text

def test_json():
    response = client.get('/json?username=BurnedOliveTree')
    assert response.status_code == 200
    assert 'BurnedOliveTree' == response.json()['name']
    assert int == type(response.json()['stars'])

def test_site_not_found():
    response = client.get('/random_url_that_does_not_exist')
    assert response.url == 'http://testserver/html'