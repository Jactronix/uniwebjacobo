#!/usr/bin/env python
"""
Utilidad de linea de comandos de Django para tareas administrativas.
Permite ejecutar el servidor, migraciones y otras tareas del proyecto.
"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uniwebjacobo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Asegurese de tenerlo instalado "
            "y disponible en su PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
