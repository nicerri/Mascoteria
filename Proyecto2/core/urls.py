from django.urls import path,include
from .views import Index
from .views import Suscribirse
from .views import OtrosPerros
from .views import IdPerro
from .views import Donaciones
from .views import CorreasPerros
from .views import Contacto
from .views import BandanasPerros
from .views import BandanasGatos
from .views import ListaProductos
from .views import FormProductos
from .views import FormModProductos
from .views import FormDelProductos
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index,name="Index"),
    path('Contacto', Contacto,name="Contacto"),
    path('OtrosPerros', OtrosPerros,name="OtrosPerros"),
    path('IdPerro', IdPerro,name="IdPerro"),
    path('Donaciones', Donaciones,name="Donaciones"),
    path('Suscribirse', Suscribirse,name="Suscribirse"),
    path('CorreasPerros', CorreasPerros,name="CorreasPerros"),
    path('BandanasPerros', BandanasPerros,name="BandanasPerros"),
    path('BandanasGatos', BandanasGatos,name="BandanasGatos"),
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