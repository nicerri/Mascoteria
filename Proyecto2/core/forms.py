from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Producto

#creo la clase para el formulario desde la base de datos
class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields=['idProducto','nombre','precio', 'img', 'caracteristicas','categoria']