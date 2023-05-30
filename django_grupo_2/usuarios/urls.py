from django.urls import path
from .views import *

urlpatterns = [
    path('alta_actividad', ActvidadAlta.as_view(), name='alta_actividad'),
    path('actividades', ListaActividades.as_view(), name='actividades'),

    path('accounts/profile/', DetailProfile.as_view(), name = 'profile'),
    path('accounts/profile_edit/', UpdateProfile.as_view(), name = 'profile_edit'),
]
