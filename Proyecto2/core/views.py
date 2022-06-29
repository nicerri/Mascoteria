from telnetlib import LOGOUT
from tokenize import group
from turtle import delay
from django import forms
from django.shortcuts import render, redirect
from core.forms import LoginForm, ProductoForm, UsuariosForm
from core.models import Producto, Usuarios
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponseRedirect
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User, Group
from rest_framework.authentication import TokenAuthentication
from rest_mascota.viewsLogin import login as api_login
#clases de api
import json
import requests
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response as apiResponse
from rest_framework.views import APIView
# Create your views here.

def Index(request):
    return render(request,'core/Index.html')

def Suscribirse(request):
    return render(request,'core/Suscribirse.html')

def Donaciones(request):
    return render(request,'core/Donaciones.html')

def Productos(request):
    return render(request,'core/Productos.html')

def Contacto(request):
    return render(request,'core/Contacto.html')


def is_staff(user):
    return user.is_authenticated


@user_passes_test(is_staff)
def ListaProductos(request):
    Productos =  Producto.objects.all()
    contexto = {
        'producto': Productos
    }
    return render(request,"core/ListaProductos.html", contexto)

def FormProductos(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST or None, request.FILES or None)
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
        formulario = ProductoForm(request.POST or None, request.FILES or None, instance = producto)
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

def user_login(request):
    datos={
        'form':LoginForm()
    }
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            usernameU = request.POST['usrN']
            passwordU = request.POST['pswrdN']
            user = authenticate(username=usernameU,password=passwordU)
            if user is not None:
                login(request,user)
                return render(request, "core/Recuperar.html")
    return render(request, "core/login.html", datos)

def Recuperar(request):
    return render(request,"core/Recuperar.html")

def newUser(request): 
    datos={
        'form':UsuariosForm()
    }
    if(request.method == 'POST'):
        form=UsuariosForm(request.POST)
        if form.is_valid():
            usernameN = form.cleaned_data.get('usrN')
            passwordN = form.cleaned_data.get('pswrdN')
            passwordN2= form.cleaned_data.get('pswrdN2')
            try:
                user = User.objects.get(username = usernameN)
            except User.DoesNotExist:
                if(passwordN == passwordN2):
                    user = User.objects.create_user(username=usernameN,email=usernameN,password=passwordN)
                    user = authenticate(username=usernameN, password=passwordN)
                    login(request,user)
                    body= {"username": usernameN ,"password" : passwordN} 
                    r = requests.post('http://127.0.0.1:8000/API/login',data=json.dumps(body))
                    print(r.text)
                    return render(request, "core/Index.html")
    return render(request,"core/newUser.html",datos)

def cerrarsesion(request):
    logout(request)
    return redirect(user_login)
    