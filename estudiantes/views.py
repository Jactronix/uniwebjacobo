"""
Vistas del proyecto uniwebjacobo.
Contiene toda la logica del servidor para los modulos
de Estudiantes y Productos.

Flujo de cada peticion:
  URL -> View (Python) -> Template (HTML) -> Response

Vistas implementadas:
  Modulo Estudiantes:
    - saludo()              -> Endpoint basico de prueba
    - home()                -> Pagina de inicio
    - registro()            -> Formulario de registro de estudiante
    - guardar_estudiante()  -> Procesa el POST del formulario
    - lista()               -> Lista de estudiantes
    - eliminar_estudiante() -> Elimina un estudiante por id
    - limpiar_lista()       -> Elimina todos los estudiantes
    - acerca()              -> Informacion del proyecto

  Modulo Productos (CRUD completo):
    - registrar_producto()  -> Formulario y guardado de producto (CREATE)
    - lista_productos()     -> Lista de productos (READ)
    - editar_producto()     -> Edicion de producto por id (UPDATE)
    - eliminar_producto()   -> Eliminar producto por id (DELETE)

Proyecto  : uniwebjacobo
Asignatura: Programacion Integrada Web
Docente   : Andres Alfonso Murgas Viloria
Autor     : Jacobo Leal Bustamante
"""

import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Estudiante, Producto


# ── MODULO ESTUDIANTES ──────────────────────────────────────

def saludo(request):
    return HttpResponse("Hola desde el servidor (Django) — Proyecto uniwebjacobo")


def home(request):
    contexto = {
        "titulo": "Home Estudiantes",
        "total_estudiantes": Estudiante.objects.count(),
    }
    return render(request, "estudiantes/home.html", contexto)


def registro(request):
    contexto = {
        "error":   request.session.pop("error_registro", None),
        "success": request.session.pop("success_registro", None),
    }
    return render(request, "estudiantes/registro.html", contexto)


def guardar_estudiante(request):
    if request.method == "POST":
        nombre   = request.POST.get("nombre", "").strip()
        edad_str = request.POST.get("edad", "").strip()
        errores  = []

        if not nombre:
            errores.append("El nombre es obligatorio.")
        elif not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', nombre):
            errores.append("El nombre solo puede contener letras y espacios.")

        if not edad_str:
            errores.append("La edad es obligatoria.")
        elif not edad_str.isdigit():
            errores.append("La edad solo puede contener numeros enteros.")
        elif int(edad_str) <= 0:
            errores.append("La edad debe ser mayor que cero.")

        if errores:
            request.session["error_registro"] = " | ".join(errores)
            return redirect("registro")

        Estudiante.objects.create(nombre=nombre, edad=int(edad_str))
        request.session["success_registro"] = f"Estudiante '{nombre}' registrado correctamente."
        return redirect("registro")

    return redirect("registro")


def lista(request):
    estudiantes = Estudiante.objects.all()
    contexto = {
        "estudiantes": estudiantes,
        "total":       estudiantes.count(),
    }
    return render(request, "estudiantes/lista.html", contexto)


def eliminar_estudiante(request, idx):
    try:
        estudiante = Estudiante.objects.get(pk=idx)
        estudiante.delete()
    except Estudiante.DoesNotExist:
        pass
    return redirect("lista")


def limpiar_lista(request):
    Estudiante.objects.all().delete()
    return redirect("lista")


def acerca(request):
    return render(request, "estudiantes/acerca.html")


# ── MODULO PRODUCTOS — CRUD COMPLETO ────────────────────────

def registrar_producto(request):
    """
    CREATE — Registrar nuevo producto.
    GET  : renderiza formulario vacio.
    POST : valida datos y guarda con Producto.objects.create().
    """
    error = None

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        precio = request.POST.get("precio", "").strip()

        if not nombre:
            error = "El nombre del producto es obligatorio."
        elif not precio:
            error = "El precio es obligatorio."
        else:
            try:
                precio_val = float(precio)
                if precio_val < 0:
                    error = "El precio no puede ser negativo."
                else:
                    Producto.objects.create(nombre=nombre, precio=precio_val)
                    return redirect("lista_productos")
            except ValueError:
                error = "El precio debe ser un numero valido."

    return render(request, "estudiantes/registro_producto.html", {"error": error})


def lista_productos(request):
    """
    READ — Listar todos los productos.
    Consulta todos los registros con Producto.objects.all().
    """
    productos = Producto.objects.all()
    return render(request, "estudiantes/lista_productos.html", {
        "productos": productos
    })


def editar_producto(request, id):
    """
    UPDATE — Editar un producto existente.
    GET  : renderiza formulario precargado con datos actuales.
    POST : valida y actualiza con producto.save().
    El parametro id identifica el registro a modificar.
    """
    try:
        producto = Producto.objects.get(pk=id)
    except Producto.DoesNotExist:
        return redirect("lista_productos")

    error = None

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        precio = request.POST.get("precio", "").strip()

        if not nombre:
            error = "El nombre del producto es obligatorio."
        elif not precio:
            error = "El precio es obligatorio."
        else:
            try:
                precio_val = float(precio)
                if precio_val < 0:
                    error = "El precio no puede ser negativo."
                else:
                    # UPDATE via ORM: modificar atributos y llamar obj.save()
                    producto.nombre = nombre
                    producto.precio = precio_val
                    producto.save()
                    return redirect("lista_productos")
            except ValueError:
                error = "El precio debe ser un numero valido."

    return render(request, "estudiantes/editar_producto.html", {
        "producto": producto,
        "error": error,
    })


def eliminar_producto(request, id):
    """
    DELETE — Eliminar un producto por id.
    Obtiene el objeto y llama obj.delete() para borrarlo de la BD.
    Redirige a la lista tras la operacion.
    """
    try:
        producto = Producto.objects.get(pk=id)
        producto.delete()
    except Producto.DoesNotExist:
        pass
    return redirect("lista_productos")
