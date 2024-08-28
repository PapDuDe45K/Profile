#!/bin/bash
set -0 errexit
#python manage.py migrate

pip install -r requirements.txt
python manage.py collectstatic 
python manage.py migrate