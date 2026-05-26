"""
Enrutamiento principal del proyecto uniwebjacobo.
Mapea cada URL a su vista correspondiente en views.py.

Flujo: URL -> View (Python) -> Template (HTML) -> Response

Modulo Estudiantes:
  /                        -> home
  /registro/               -> registro
  /lista/                  -> lista
  /acerca/                 -> acerca
  /guardar/                -> guardar_estudiante
  /eliminar/<id>/          -> eliminar_estudiante
  /lista/limpiar/          -> limpiar_lista
  /saludo/                 -> saludo (endpoint de prueba)

Modulo Productos (CRUD completo):
  /productos/              -> lista_productos    (READ)
  /productos/registro/     -> registrar_producto (CREATE)
  /productos/editar/<id>/  -> editar_producto    (UPDATE)
  /productos/eliminar/<id>/-> eliminar_producto  (DELETE)

Proyecto  : uniwebjacobo
Asignatura: Programacion Integrada Web
Docente   : Andres Alfonso Murgas Viloria
Autor     : Jacobo Leal Bustamante
"""

from django.contrib import admin
from django.urls import path
from estudiantes.views import (
    home,
    registro,
    lista,
    acerca,
    guardar_estudiante,
    eliminar_estudiante,
    limpiar_lista,
    saludo,
    registrar_producto,
    lista_productos,
    editar_producto,
    eliminar_producto,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),

    # Modulo Estudiantes
    path('', home, name='home'),
    path('registro/', registro, name='registro'),
    path('lista/', lista, name='lista'),
    path('acerca/', acerca, name='acerca'),
    path('guardar/', guardar_estudiante, name='guardar'),
    path('eliminar/<int:idx>/', eliminar_estudiante, name='eliminar'),
    path('lista/limpiar/', limpiar_lista, name='limpiar'),

    # Modulo Productos - CRUD completo
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/registro/', registrar_producto, name='registrar_producto'),
    path('productos/editar/<int:id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
]
