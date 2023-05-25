"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('planeadores_mdp.urls')),

    path('accounts/', include('seguridad.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# encontrar manera elegante para la inclusión de 'media'
# nota: toma la primera que encuentra, mmm, un django facil.
