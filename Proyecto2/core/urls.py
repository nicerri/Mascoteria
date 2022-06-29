from unicodedata import name
from django.urls import path,include
from .views import cerrarsesion
from .views import Index
from .views import Suscribirse
from .views import Donaciones
from .views import Productos
from .views import Contacto
from .views import ListaProductos
from .views import FormProductos
from .views import FormModProductos
from .views import FormDelProductos
from .views import Recuperar
from .views import user_login
from .views import newUser
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index,name="Index"),
    path('Contacto', Contacto,name="Contacto"),
    path('login', user_login, name='login'),
    path('newUser/', newUser, name='newUser'),
    path('Recuperar/', Recuperar, name='Recuperar'),
    path('logout/',cerrarsesion, name='cerrarsesion'),
    path('Donaciones', Donaciones,name="Donaciones"),
    path('Suscribirse', Suscribirse,name="Suscribirse"),
    path('Productos', Productos,name="Productos"),
    path('ListaProductos', ListaProductos, name="ListaProductos"),
    path('FormProductos', FormProductos, name="FormProductos"),
    path('FormModProductos/<id>', FormModProductos, name="FormModProductos"),
    path('FormDelProductos/<id>', FormDelProductos, name="FormDelProductos"),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="InicioSeccion")),
    path('logout', LogoutView.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)