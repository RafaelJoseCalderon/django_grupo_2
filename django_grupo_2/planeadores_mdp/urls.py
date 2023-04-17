from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('escuela_de_vuelo', views.escuela_de_vuelo, name='escuela_de_vuelo'),
    path('vuelo_de_bautismo', views.vuelo_de_bautismo, name='vuelo_de_bautismo'),
    path('only_socios', views.only_socios, name='only_socios'),
    path('preguntas_frecuentes', views.preguntasFrecuentes, name='preguntas_frecuentes'),
    path('contacto', views.contacto, name='contacto'),
]
