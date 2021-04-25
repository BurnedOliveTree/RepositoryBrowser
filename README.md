# Repository Browser

A small and simple Python web application that let's you browse repositories of every user on GitHub.

## Setup

There are 2 ways to launch this application: using Docker or by installing needed libraries directly on your computer.

It is also recommended to add a personal access token, which will lift the limit from 60 requests per hour to 1500, but it's not required.

### Docker

In order to follow these steps you need [Docker](https://www.docker.com) installed on your computer.

Firstly you need to create an image by executing this command:

```
docker build -t burnedolivetree/pythonfastapi:1.0 .
```
Then, to launch the application, execute this command:

```
docker run -p 8000:8000 burnedolivetree/repositorybrowser:1.0
```

You will find your launched application at http://127.0.0.1:8000

### Direct

To follow these steps, app requires Python installed on your machine along with some libraries with it.
If you do not have Python on your system, please install it from the official [site](https://www.python.org/downloads/).

To install needed libraries (or to simply check if you have them) you need to run these commands:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

To launch it, you need to execute following command (in directory where you cloned this repository to):

```
uvicorn main:app
```
And then, please open your preferred browser and go the link that was shown in terminal (by default it should be http://127.0.0.1:8000)

### Personal Access Token

If you want to be able to make more requests to GitHub per hour, you need to go [GitHub settings](https://github.com/settings/tokens), create a new token (no need to select any scope), create a new file 'token.txt' in the same directory as this cloned repository, and then paste the token into this file.

## Notes

This application is set up to redirect user to a website by default, but it is also possible to get a *json* file from it. In order to access it, you need to go to http://127.0.0.1:8000/json?username=name, where *name* is a GitHub's user username. 

## Possible Enhancements

* Multiple website themes.
    * Themes would be stored in small CSS files like *dark.css*.
    * Switch / menu would have to be added to *index.html* to be able to select them.
* Extend functionality to work with GitLab and BitBucket