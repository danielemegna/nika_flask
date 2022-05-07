FROM python:3.10.4-alpine

RUN pip install Flask==2.1.2

# FLASK_ENV=development flask run -h 0.0.0.0
