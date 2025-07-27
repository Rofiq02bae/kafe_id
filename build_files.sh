#!/bin/bash
# Build script for Vercel deployment

# Install dependencies
pip install -r requirements.txt

# Make migrations 
python manage.py makemigrations

# Migrasi database
python manage.py migrate

# Kumpulkan static files
python manage.py collectstatic --noinput
