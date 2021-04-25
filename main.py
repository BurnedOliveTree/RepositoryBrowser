from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
import requests
import os.path

app = FastAPI()
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
app.mount("/resources", StaticFiles(directory="resources"), name="resources")
templates = Jinja2Templates(directory=".")


header = {}
if os.path.isfile('token.txt'):
    with open('token.txt') as file:
        header['Authorization'] = 'token '+file.read()


class ApiResponse():
    def __init__(self, username: str):
        def get_data(username: str) -> (dict, int):
            if username == None:
                return {}, 200
            if username == '':
                return {}, 204
            page = 1
            github_response = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100&page={page}', headers=header)
            if github_response.status_code == 404:
                return {'name': username, 'err': 'Please enter a valid GitHub username'}, 404
            else:
                repos = []
                stars = 0
                while(len(github_response.json()) > 0):
                    for repo in github_response.json():
                        repos.append([repo['name'], repo['stargazers_count']])
                        stars += repo['stargazers_count']
                    page += 1
                    github_response = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100&page={page}', headers=header)
                return {'name': username, 'stars': stars, 'repos': repos}, 200
        
        self.json, self.status_code = get_data(username)


@app.get("/")
def root(request: Request, username: str=None):
    return RedirectResponse(url=f"/html{'?username='+username if username is not None else ''}")

@app.get('/html', response_class=HTMLResponse)
def site(request: Request, username: str=None):
    response = ApiResponse(username)
    response.json['request'] = request
    return templates.TemplateResponse('index.html', response.json, status_code=response.status_code)

@app.get('/json', response_class=JSONResponse)
def api(username: str=None):
    response = ApiResponse(username)
    return JSONResponse(content=response.json, status_code=response.status_code)

@app.exception_handler(StarletteHTTPException)
def exception_handler(request: Request, exception):
    return RedirectResponse(url="/html")