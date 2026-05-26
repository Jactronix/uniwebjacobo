"""
Configuracion de la aplicacion modular 'estudiantes'.
Esta app contiene los modulos de Estudiantes y Productos.
"""
from django.apps import AppConfig


class EstudiantesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estudiantes'
