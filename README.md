# Repository Browser

A small and simple Python web application that let's you browse repositories of every user on GitHub.

App requires Python installed on your machine along with some libraries with it.
If you do not have Python on your system, please follow these official [instructions](https://www.python.org/downloads/).

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