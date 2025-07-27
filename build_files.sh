#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate --run-syncdb

# Collect static files
python manage.py collectstatic --noinput --clear
