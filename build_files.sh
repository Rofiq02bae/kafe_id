#!/bin/bash
# Build script for Vercel deployment

# Aktifkan virtualenv jika diperlukan
# source env/bin/activate

# Migrasi database
python manage.py migrate

# Kumpulkan static files
python manage.py collectstatic --noinput
