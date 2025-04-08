"""
WSGI config for crm_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
path = '/home/emre77/deneme'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'crm_project.settings'

# Set the 'application' variable so that PythonAnywhere can find it
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
