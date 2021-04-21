from fastapi import FastAPI, Response
import requests

app = FastAPI()

@app.get('/', status_code=200)
def root():
    return {'message': 'Hello world'}

@app.get('/repository')
def repository(response: Response, username: str=None):
    if username == None:
        response.status_code = 400
        return 'Please enter a GitHub username'
    github_response = requests.get(f'https://api.github.com/users/{username}/repos')
    if github_response.status_code == 404:
        response.status_code = 404
        return 'Please enter a valid GitHub username'
    else:
        response.status_code = 200
        return github_response.json()