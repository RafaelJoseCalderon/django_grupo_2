from django import forms
from django.contrib import admin

from .models import Instructor
from .models import Piloto
from .models import Planeador
from .models import Remolcador
from .models import Actividad


class ChoiceFieldMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget.can_add_related = False
        self.widget = forms.Select(
            attrs = {'style': 'width: 500px'}
        )


class UsuarioChoiceField(ChoiceFieldMixin, forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{self.label}: {obj.last_name}, {obj.first_name}"


class AeronaveChoiceField(ChoiceFieldMixin, forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{self.label}: {obj.nombre}"


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['get_instructor', 'get_piloto', 'get_remolcador', 'get_planeador']

    def get_instructor(self, actividad):
        instructor = actividad.instructor
        return f'{instructor.last_name}, {instructor.first_name}'

    def get_piloto(self, actividad):
        piloto = actividad.piloto
        return f'{piloto.last_name}, {piloto.first_name}'

    def get_remolcador(self, actividad):
        remolcador = actividad.remolcador
        return f'{remolcador.nombre}'

    def get_planeador(self, actividad):
        planeador = actividad.planeador
        return f'{planeador.nombre}'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        for field in form.base_fields.values():
            field.widget.can_add_related = False
            field.widget.can_change_related = False
            field.widget.can_delete_related = False

        return form

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'instructor':
            return UsuarioChoiceField(
                label = 'Instructor',
                queryset = Instructor.objects.all()
            )

        if db_field.name == 'piloto':
            return UsuarioChoiceField(
                label = 'Piloto',
                queryset = Piloto.objects.all()
            )

        if db_field.name == 'remolcador':
            return AeronaveChoiceField(
                label = 'Remolcador',
                queryset = Remolcador.objects.all()
            )

        if db_field.name == 'planeador':
            return AeronaveChoiceField(
                label = 'Planeador',
                queryset = Planeador.objects.all()
            )

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Instructor, Piloto)
class InstructorPilotoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'dni']


@admin.register(Planeador, Remolcador)
class AeronaveAdmin(admin.ModelAdmin):
    list_display = ['nombre']
