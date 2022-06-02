from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='IdCategorias')
    nombreCategoria = models.CharField(max_length=50,verbose_name='NombreCategorias')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.CharField(max_length=6,primary_key=True, verbose_name='IdProducto')
    nombre = models.CharField(max_length=20, null=True, blank=True, verbose_name='Nombre')
    precio = models.CharField(max_length=20, verbose_name='Precio')
    caracteristicas = models.CharField(max_length=20,null=True, blank=True, verbose_name='Caracteristicas')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idProducto
