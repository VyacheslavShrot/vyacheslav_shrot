#!/bin/bash

python /portfolio/src/manage.py makemigrations
python /portfolio/src/manage.py migrate

#gunicorn -w ${WSGI_WORKERS} -b 0:${WSGI_PORT} --chdir ./src config.wsgi:application --reload --log-level=${WSGI_LOG_LEVEL}
python /portfolio/src/manage.py runserver 0:8000