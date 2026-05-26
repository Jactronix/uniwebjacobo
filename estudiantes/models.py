"""
Modelos del proyecto uniwebjacobo.
Define la estructura de las tablas en la base de datos SQLite
mediante el ORM de Django (Object Relational Mapping).

Cada clase representa una tabla:
  - Estudiante → tabla estudiantes_estudiante
  - Producto   → tabla estudiantes_producto

Cada instancia de una clase representa una fila de esa tabla.

Proyecto  : uniwebjacobo
Asignatura: Programacion Integrada Web
Docente   : Andres Alfonso Murgas Viloria
Autor     : Jacobo Leal Bustamante
"""

from django.db import models


class Estudiante(models.Model):
    """
    Modelo Estudiante.
    Representa la tabla de estudiantes en la base de datos.

    Campos:
      - nombre: texto, maximo 100 caracteres
      - edad  : numero entero
    """
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """
    Modelo Producto.
    Representa la tabla de productos en la base de datos.

    Campos:
      - nombre: texto, maximo 100 caracteres
      - precio: decimal con hasta 10 digitos y 2 decimales
    """
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
