#!/bin/sh

export FLASK_ENV=test
export FLASK_DEBUG=1
flask init-db
flask write-fixtures
flask run
