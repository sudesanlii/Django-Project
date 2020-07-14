"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import blog
from django.core.wsgi import get_wsgi_application
DJANGO_SETTINGS_MODULE=blog.settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = get_wsgi_application()