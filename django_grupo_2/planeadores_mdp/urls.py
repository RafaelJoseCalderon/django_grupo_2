from django.urls import path
from .views import Home, Aeronave, Institucion, SoloSocios, Contacto

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('aeronaves', Aeronave.as_view(), name='aeronaves'),
    path('institucion', Institucion.as_view(), name='institucion'),
    path('solo_socios', SoloSocios.as_view(), name='solo_socios'),
    path('contacto', Contacto.as_view(), name='contacto'),
]
