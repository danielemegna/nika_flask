#!/bin/sh

BASEDIR=$(dirname $0)
/bin/sh ${BASEDIR}/setup-test-db.sh

export FLASK_ENV=test
export FLASK_DEBUG=1
flask run
