from django.urls import path
from .views import *


urlpatterns = [
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % redireccion                                                           %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    path(
        route = '',
        view = redireccion,
        name = 'usuario'
    ),

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % para todos los usuarios                                               %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % para los instructors                                                  %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    path(
        route = 'planes-de-vuelo',
        view = PlanesDeVuelo.as_view(),
        name = 'planes-de-vuelo'
    ),
    path(
        route = 'plan-de-vuelo/<int:pk>',
        view = DetallePlanDeVuelo.as_view(),
        name = 'plan-de-vuelo'
    ),
    path(
        route = 'alta-plan-de-vuelo',
        view = AltaPlanDeVuelo.as_view(),
        name = 'alta-plan-de-vuelo'
    ),
    path(
        route = 'baja-plan-de-vuelo/<int:pk>',
        view = BajaPlanDeVuelo.as_view(),
        name = 'baja-plan-de-vuelo'
    ),
    path(
        route = 'modi-plan-de-vuelo/<int:pk>',
        view = ModiPlanDeVuelo.as_view(),
        name = 'modi-plan-de-vuelo'
    ),
    path(
        route = 'actividades-i',
        view = ActividadesInstructor.as_view(),
        name = 'actividades-i'
    ),
    path(
        route = 'actividad/<int:pk>',
        view = DetalleActividad.as_view(),
        name = 'actividad'
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

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % para los pilotos                                                      %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    path(
        route = 'actividades-p',
        view = ActividadesPiloto.as_view(),
        name = 'actividades-p'
    ),
]
