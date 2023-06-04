from django.urls import path
from .views import *

urlpatterns = [
    path('alta_actividad', ActvidadAlta.as_view(), name='alta_actividad'),
    path('actividades', ListaActividades.as_view(), name='actividades'),

    path('usuario/perfil/', DetallePerfil.as_view(), name = 'perfil'),
    path('usuario/editar_perfil/', ActualizacionPerfil.as_view(), name = 'editar_perfil'),
]
