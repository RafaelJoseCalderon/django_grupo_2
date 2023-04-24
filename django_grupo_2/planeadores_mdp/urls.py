from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aeronaves', views.aeronaves, name='aeronaves'),
    path('institucion', views.institucion, name='institucion'),
    path('only_socios', views.only_socios, name='only_socios'),
    # path('preguntas_frecuentes', views.preguntasFrecuentes, name='preguntas_frecuentes'),
    path('contacto', views.contacto, name='contacto'),
]
