from django.urls import path
from .views import *

urlpatterns = [
    path('alta_actividad', ActvidadAlta.as_view(), name='alta_actividad'),
    path('actividades', ListaActividades.as_view(), name='actividades'),
]
