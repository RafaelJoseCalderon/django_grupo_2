from django.urls import path
from .views import *

urlpatterns = [
    # path('', redireccion, name='usuarios'),

    path('alta_actividad', ActvidadAlta.as_view(), name='alta_actividad'),
    path('actividades', ListaActividades.as_view(), name='actividades'),

    path('perfil/', DetallePerfil.as_view(), name = 'perfil'),
    path('editar_perfil/', ActualizacionPerfil.as_view(), name = 'editar_perfil'),
]
