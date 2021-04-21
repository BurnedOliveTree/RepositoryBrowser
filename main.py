from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/', status_code=200)
def root():
    return {'message': 'Hello world'}

@app.get('/repository')
def repository(username: str=None):
    if username == None:
        return 'Please enter a GitHub username'
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    if response.status_code == 404:
        return 'Please enter a valid GitHub username'
    return response.json()