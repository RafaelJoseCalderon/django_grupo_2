from django.contrib import admin
from .models import Aeronave


@admin.register(Aeronave)
class PropiedadAdmin(admin.ModelAdmin):
    pass