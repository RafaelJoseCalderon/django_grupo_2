from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('planeadores', Planeador.as_view(), name='planeadores'),
    path('remolcadores', Remolcador.as_view(), name='remolcadores'),
    path('institucion', Institucion.as_view(), name='institucion'),
    path('contacto', Contacto.as_view(), name='contacto'),
]
