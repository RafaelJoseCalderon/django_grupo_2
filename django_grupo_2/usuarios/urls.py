from django.urls import path
from .views import *


urlpatterns = [
    # redireccion
    path(
        route = '',
        view = redireccion,
        name = 'usuario'
    ),

    # para todos los usuarios
    path(
        route = 'perfil/',
        view = DetallePerfil.as_view(),
        name = 'perfil'
    ),
    path(
        route = 'editar-perfil/',
        view = ActualizacionPerfil.as_view(),
        name = 'editar-perfil'
    ),

    # para los instructors
    path(
        route = 'actividades-i',
        view = ActividadesInstructor.as_view(),
        name = 'actividades-i'
    ),
    path(
        route = 'alta-actividad',
        view = AltaActvidad.as_view(),
        name = 'alta-actividad'
    ),
    path(
        route = 'baja-actividad/<int:pk>',
        view = BajaActvidad.as_view(),
        name = 'baja-actividad'
    ),
    path(
        route = 'modi-actividad/<int:pk>',
        view = ModiActvidad.as_view(),
        name = 'modi-actividad'
    ),

    # para los pilotos
    path(
        route = 'actividades-p',
        view = ActividadesPiloto.as_view(),
        name = 'actividades-p'
    ),
]
