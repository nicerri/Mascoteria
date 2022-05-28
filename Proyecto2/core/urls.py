from django.urls import path
from .views import home
from .views import Suscribirse
from .views import OtrosPerros
from .views import IdPerro
from .views import Donaciones
from .views import CorreasPerros
from .views import Contacto
from .views import BandanaPerros

urlpatterns = [
    path('', home,name="index"),
    path('Contacto', Contacto,name="Contacto"),
    path('OtrosPerros', OtrosPerros,name="OtrosPerros"),
    path('IdPerro', IdPerro,name="IdPerro"),
    path('Donaciones', Donaciones,name="Donaciones"),
    path('Suscribirse', Suscribirse,name="Suscribirse"),
    path('CorreasPerros', CorreasPerros,name="CorreasPerros"),
    path('BandanaPerros', BandanaPerros,name="BandanaPerros"),
]