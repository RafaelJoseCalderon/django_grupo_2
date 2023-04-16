from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imagenes', views.imagenes, name='imagenes'),
    path('tarifas', views.tarifas, name='tarifas'),
    path('preguntas_frecuentes', views.preguntasFrecuentes, name='preguntas_frecuentes'),
    path('formulario_contacto', views.formularioContacto, name='formulario_contacto'),
]
