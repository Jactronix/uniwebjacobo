#!/bin/bash
# Script que ejecuta Vercel durante el build
# Instala dependencias, recolecta estaticos y aplica migraciones

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
