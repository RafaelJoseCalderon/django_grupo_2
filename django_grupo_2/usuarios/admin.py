from django.contrib import admin

from .models import Instructor, Piloto, Planeador, Remolcador


@admin.register(Instructor, Piloto, Planeador, Remolcador)
class AeroclubAdmin(admin.ModelAdmin):
    pass