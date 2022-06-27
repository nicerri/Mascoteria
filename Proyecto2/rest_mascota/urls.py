from django.urls import path
from rest_mascota.views import lista_producto, detalle_producto
from rest_mascota.viewsLogin import login

urlpatterns = [
    path('lista_producto', lista_producto, name= "lista_producto"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login', login, name='login'),
]