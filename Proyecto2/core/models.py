from pyexpat import model
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='idCategorias')
    nombreCategoria = models.CharField(max_length=50,verbose_name='NombreCategorias')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='idProducto')
    nombre = models.CharField(max_length=20, null=True, blank=True, verbose_name='Nombre')
    precio = models.CharField(max_length=20, verbose_name='Precio')
    img=models.ImageField(upload_to = 'core/static/core/img/',null=True,verbose_name='Imagen')
    caracteristicas = models.CharField(max_length=50,null=True, blank=True, verbose_name='Caracteristicas')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idProducto

class Usuarios(models.Model):
    usrN= models.CharField(max_length=30,verbose_name="Nombre de Usuario")
    pswrdN= models.CharField(max_length=15, verbose_name="Contraseña")
    pswrdN2=models.CharField(max_length=15, verbose_name="Contraseña2")
