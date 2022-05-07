## Dev Notes

```console
$ docker run --rm -itp 5000:5000 -v $PWD:/app -w /app python:3.10.4-alpine sh
# pip install Flask==2.1.2
# python db/init_db.py
# FLASK_ENV=development flask run -h 0.0.0.0
```
