from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
app.mount("/styles", StaticFiles(directory="styles"), name="styles")

templates = Jinja2Templates(directory=".")

@app.get('/', response_class=HTMLResponse)
def root(request: Request, username: str=None):
    if username == None or username == '':
        return templates.TemplateResponse('index.html', {'request': request, 'msg': ''}, status_code=400)
    github_response = requests.get(f'https://api.github.com/users/{username}/repos')
    if github_response.status_code == 404:
        return templates.TemplateResponse('index.html', {'request': request, 'msg': 'Please enter a valid GitHub username'}, status_code=404)
    else:
        repos = []
        stars = 0
        for repo in github_response.json():
            repos.append([repo['name'], repo['stargazers_count']])
            stars += repo['stargazers_count']
        return templates.TemplateResponse('index.html', {'request': request, 'msg': username, 'stars': stars, 'repos': repos}, status_code=200)