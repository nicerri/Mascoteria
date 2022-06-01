from django.shortcuts import render, redirect
from .models import Producto
from core.forms import ProductoForm
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
    producto= Producto.objects.all()
    datos = {
        'producto': producto
    }
    return render(request, 'core/ListaProductos.html', datos)

def FormProductos(request):
    contexto={
        'form': ProductoForm()
    }
    if request.method=='POST':
        formulario=ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje']="Guardados Correctamente"
    return render(request,'core/FormProductos.html', contexto)    

def FormModProductos(request,id):
    producto= Producto.objects.get(idProducto=id)
    contexto={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje']="Modificado Correctamente"
    return render(request,'core/FormModProductos.html', contexto)

def FormDelProductos(request,id):
    producto= Producto.objects.get(producto=id)
    producto.delete()
    return redirect(to='ListaProductos')