"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

import environ
from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve().parent.parent

# READING ENV
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE"))

application = get_wsgi_application()
