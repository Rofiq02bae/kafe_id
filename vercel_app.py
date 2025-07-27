"""
This file is used by Vercel to serve the application.
"""
from app.wsgi import application

# Handler for Vercel
app = application
