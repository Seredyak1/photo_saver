#!/bin/bash

python /code/manage.py collectstatic --no-input
python /code/manage.py migrate
/usr/bin/supervisord

