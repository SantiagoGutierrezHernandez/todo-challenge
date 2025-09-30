#!/usr/bin/env bash

cd app

python3 manage.py collectstatic --noinput

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

gunicorn -b $GUNICORN_ADDRESS --workers $WORKERS --timeout $TIMEOUT todo.wsgi