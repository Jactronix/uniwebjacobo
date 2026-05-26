"""
Configuracion principal del proyecto uniwebjacobo.
Soporta desarrollo local (DEBUG=True) y produccion en Vercel (DEBUG=False).

Proyecto  : uniwebjacobo
Asignatura: Programacion Integrada Web
Docente   : Andres Alfonso Murgas Viloria
Autor     : Jacobo Leal Bustamante
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# En produccion (Vercel) se debe definir la variable de entorno SECRET_KEY
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-uniwebjacobo-programacion-integrada-web-2026'
)

# DEBUG=False en produccion. Vercel define VERCEL=1 automaticamente
DEBUG = os.environ.get('VERCEL', '') == ''

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',
    '.now.sh',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'estudiantes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise: sirve archivos estaticos en produccion sin servidor aparte
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uniwebjacobo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'uniwebjacobo.wsgi.application'

# Base de datos SQLite para desarrollo
# En produccion con Vercel el sistema de archivos es efimero;
# para persistencia real se recomienda migrar a PostgreSQL (Neon, Supabase, etc.)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# Archivos estaticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# WhiteNoise comprime y cachea estaticos en produccion
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
