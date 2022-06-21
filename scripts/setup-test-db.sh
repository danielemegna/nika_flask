#!/bin/sh

export FLASK_ENV=test
flask init-db
flask write-fixtures
