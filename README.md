## Studying Python and Flask

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.

- github.com/pallets/flask/
- flask.palletsprojects.com

### Dev Notes

Setup a temporary dev docker container:

```console
$ docker run --rm -itp 5000:5000 -v $PWD:/app -w /app python:3.10.4-alpine sh
# pip install Flask==2.1.2
```

Init an empty db:

```console
# flask init-db
```
or
```console
# python db/init_db.py
```

Optionally fill db with some fixture data:

```console
# flask write-fixtures
```

Start the application:
```console
# FLASK_ENV=development flask run -h 0.0.0.0
```
