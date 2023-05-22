from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('planeadores', Planeador.as_view(), name='planeadores'),
    path('remolcadores', Remolcador.as_view(), name='remolcadores'),
    path('institucion', Institucion.as_view(), name='institucion'),
    path('contacto', Contacto.as_view(), name='contacto'),

    path('alta_actividad', ActvidadAlta.as_view(), name='alta_actividad'),
    path('actividades', ListaActividades.as_view(), name='actividades'),
]
