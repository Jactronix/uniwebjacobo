"""
Punto de entrada WSGI para servidores web en produccion.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uniwebjacobo.settings')
application = get_wsgi_application()
