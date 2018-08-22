[![Build Status](https://travis-ci.org/frol/flask-restplus-server-example.svg)](https://travis-ci.org/alfredosilvestre-natixis/flask-restplus-pymongo-jumpstart.svg)
[![Coverage Status](https://coveralls.io/repos/github/alfredosilvestre-natixis/flask-restplus-pymongo-jumpstart/badge.svg?branch=master)](https://coveralls.io/github/alfredosilvestre-natixis/flask-restplus-pymongo-jumpstart?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cd8bbc6d04a54f1cac30fd7e02344e94)](https://www.codacy.com/project/alfredosilvestre-natixis/flask-restplus-pymongo-jumpstart/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alfredosilvestre-natixis/flask-restplus-pymongo-jumpstart&amp;utm_campaign=Badge_Grade_Dashboard)

Flask-RESTplus PyMongo Jumpstart
==========================

This project is an example on how to start a project using Flask-RESTplus
and PyMongo

The project is based on a divisional structure so it is easy to extend.

The following features were implemented:

* Blueprints for modules and namespaces for sub-modules (imported recursively
from sub-folders)
* Models using Flask-RESTplus namespaces
* Basic MongoDB operations
* Different configurations depending on the environment
* Documentation via Swagger
* PyLint and PyTest with 100% coverage
* Application logs



Dependencies
------------

* [**Python 3.7+**](https://www.python.org/)
* [**flask-restplus**](https://github.com/noirbizarre/flask-restplus) (+
  [*flask*](http://flask.pocoo.org/))
* [**Swagger-UI**](https://github.com/swagger-api/swagger-ui)
* [**flask-pymongo**](https://flask-pymongo.readthedocs.io/en/latest/) (+
  [*pymongo*](https://api.mongodb.com/python/current/))
* [**pytest-cov**](https://pytest-cov.readthedocs.io/en/latest/) (+
  [*pytest*](https://docs.pytest.org/en/latest/))
* [**pylint**](https://www.pylint.org/)


Installation
------------

### From sources

#### Clone the Project

```bash
$ git clone https://github.com/alfredosilvestre-natixis/flask-restplus-pymongo-jumpstart.git
```

#### Setup Environment

It is recommended to use virtualenv to manage Python dependencies. PyCharm
is also a good IDE to start.

```bash
$ pip install -r requirements.txt
```


#### Run Server

```bash
$ python run.py
```

#### Linting

```bash
$ pylint app
``` 

#### Testing

```bash
$ pytest --cov=app
```

References
============

This project was based on some of these great resources 

* [Flask Bookshelf](https://github.com/damyanbogoev/flask-bookshelf)
* [RESTful API Server Example](https://github.com/frol/flask-restplus-server-example)
* [Full-stack tutorial  -  2 : Flask + mongoDB](https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-ee316a46e876)
* [Building beautiful REST APIs using Flask, Swagger UI and Flask-RESTPlus](http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/)