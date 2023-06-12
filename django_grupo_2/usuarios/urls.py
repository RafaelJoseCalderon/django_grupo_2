from django.urls import path
from .views import *

urlpatterns = [
    path('usuario', redireccion, name='usuario'),

    path('usuario/perfil/', DetallePerfil.as_view(), name = 'perfil'),
    path('usuario/editar_perfil/', ActualizacionPerfil.as_view(), name = 'editar_perfil'),

    path('instructor/actividades', ActividadesInstructor.as_view(), name='actividades_instructor'),
    path('instructor/alta_actividad', AltaActvidad.as_view(), name='alta_actividad'),
    path('instructor/baja-actividad/<int:pk>', BajaActvidad.as_view(), name='baja-actividad'),
    path('instructor/modi-actividad/<int:pk>', ModiActvidad.as_view(), name='modi-actividad'),

    path('piloto/actividades', ActividadesPiloto.as_view(), name='actividades_piloto'),
]
