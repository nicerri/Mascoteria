from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Producto, Usuarios

#creo la clase para el formulario desde la base de datos
class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields=['idProducto','nombre','precio', 'img', 'caracteristicas','categoria']

class UsuariosForm(ModelForm):
    #se da formato a cada uno de los campos dentro de la forma
    usrN = forms.CharField(widget=forms.EmailInput(attrs={'class':'login-username','placeholder':'Email'}),label='')
    pswrdN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    pswrdN2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Repetir Contraseña'}),label='')
    class Meta:
        #se asigna modelo y orden de aparicion en html
        model = Usuarios
        fields= ['usrN','pswrdN','pswrdN2']

class LoginForm(ModelForm):
    usrN = forms.CharField(widget=forms.EmailInput(attrs={'class':'login-username','placeholder':'Email'}),label='')
    pswrdN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-password','placeholder':'Contraseña'}),label='')
    class Meta:
        model=Usuarios
        fields= ['usrN','pswrdN']