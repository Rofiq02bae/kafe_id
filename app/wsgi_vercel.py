"""
WSGI config for app project for Vercel deployment.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# This application object is used by Vercel
application = get_wsgi_application()

# For Vercel deployment
app = application
