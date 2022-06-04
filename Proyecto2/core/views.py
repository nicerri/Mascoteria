from django.shortcuts import render, redirect
from core.forms import ProductoForm
from .models import Producto
# Create your views here.

def Index(request):
    return render(request,'core/Index.html')

def Suscribirse(request):
    return render(request,'core/Suscribirse.html')

def OtrosPerros(request):
    return render(request,'core/OtrosPerros.html')

def IdPerro(request):
    return render(request,'core/Idperro.html')

def Donaciones(request):
    return render(request,'core/Donaciones.html')

def CorreasPerros(request):
    return render(request,'core/CorreasPerros.html')

def Contacto(request):
    return render(request,'core/Contacto.html')

def BandanasPerros(request):
    return render(request,'core/BandanasPerros.html')

def BandanasGatos(request):
    return render(request,'core/BandanasGatos.html')

def ListaProductos(request):
    Productos =  Producto.objects.all() #select * from Producto
    contexto = {
        'producto': Productos
    }
    return render(request,"core/ListaProductos.html", contexto)

def FormProductos(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Se guardó el producto'
        else:
            datos['mensaje'] = 'NO se guardó el producto'
 
    return render(request,"core/FormProductos.html", datos)

def FormModProductos(request, id):
    producto = Producto.objects.get(idProducto = id)

    datos = {
        'form': ProductoForm(instance = producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance = producto)

        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Se modificó el producto'
        else:
            datos['mensaje'] = 'NO se modificó el producto'

    return render(request,"core/FormModProductos.html", datos)

def FormDelProductos(request, id):
    productos = Producto.objects.get(idProducto = id)
    productos.delete() #delete de la BD
    return redirect(to='ListaProductos')