# uniwebjacobo — Programacion Integrada Web

Proyecto Django desarrollado para la asignatura **Programacion Integrada Web**
en la Corporacion Universitaria Minuto de Dios (UNIMINUTO).

**Docente:** Andres Alfonso Murgas Viloria  
**Autor:** Jacobo Leal Bustamante  

---

## Contenido del proyecto

Implementa el modelo arquitectonico Cliente → Servidor Django → Vista → Respuesta HTTP,
cubriendo todos los temas del segundo corte:

- Programacion del lado del servidor con Python/Django
- Diseño de vistas web (capa de presentacion): HTML + CSS + JavaScript
- ORM (Object Relational Mapping) con SQLite
- CRUD completo (Create, Read, Update, Delete)
- Procesos transaccionales con `@transaction.atomic`
- Servicios web: HTTP, endpoints, JSON

## Modulos

### Estudiantes
| URL | Metodo | Descripcion |
|-----|--------|-------------|
| `/` | GET | Pagina de inicio |
| `/registro/` | GET | Formulario de registro |
| `/guardar/` | POST | Guarda estudiante en BD |
| `/lista/` | GET | Lista de estudiantes |
| `/eliminar/<id>/` | GET | Elimina estudiante |
| `/lista/limpiar/` | GET | Limpia toda la lista |
| `/acerca/` | GET | Informacion del proyecto |

### Productos (CRUD completo)
| URL | Metodo | Operacion CRUD |
|-----|--------|----------------|
| `/productos/` | GET | READ — lista todos |
| `/productos/registro/` | GET/POST | CREATE — registrar |
| `/productos/editar/<id>/` | GET/POST | UPDATE — editar |
| `/productos/eliminar/<id>/` | GET | DELETE — eliminar |

---

## Ejecucion local

```bash
# Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Ejecutar servidor
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000

---

## Despliegue en Vercel

1. Subir el proyecto a GitHub
2. Importar el repositorio en [vercel.com](https://vercel.com)
3. Vercel detecta `vercel.json` y ejecuta `build_files.sh` automaticamente
4. Configurar la variable de entorno `SECRET_KEY` en Vercel Dashboard

> **Nota sobre la base de datos:** Vercel tiene sistema de archivos efimero.
> SQLite funciona para demostracion pero los datos se reinician con cada deploy.
> Para persistencia en produccion se recomienda conectar a PostgreSQL
> (Neon, Supabase o Vercel Postgres).

---

## Estructura del proyecto

```
uniwebjacobo/
├── vercel.json                  # Configuracion de despliegue Vercel
├── build_files.sh               # Script de build para Vercel
├── requirements.txt             # Dependencias Python
├── manage.py
├── db.sqlite3
├── uniwebjacobo/
│   ├── settings.py              # Configuracion (dev + produccion)
│   ├── urls.py                  # Enrutamiento principal
│   └── wsgi.py
└── estudiantes/
    ├── models.py                # Modelos ORM: Estudiante, Producto
    ├── views.py                 # Vistas: logica del servidor
    └── templates/
        └── estudiantes/
            ├── base.html
            ├── home.html
            ├── registro.html
            ├── lista.html
            ├── registro_producto.html
            ├── lista_productos.html
            ├── editar_producto.html
            └── acerca.html
```
