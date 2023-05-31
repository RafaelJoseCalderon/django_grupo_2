from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from herramientas.widgets import ClearableFileInput

from .models import Perfil
from .models import Actividad


class InitFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class PerfilForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen']
        widgets = {
            'imagen': ClearableFileInput()
        }

    def __init__(self, *args, **kwargs):

        print(ClearableFileInput().media)

        kwargs['instance'] = kwargs['instance'].perfil
        super().__init__(*args, **kwargs)


class UsuarioPerfilForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.perfil = PerfilForm(*args, **kwargs)
 
        for field in self.fields.values():
            field.required = True

    def is_valid(self):
        return super().is_valid() and self.perfil.is_valid()

    # como diantres se hace el atomic aca!!!
    def save(self):
        perfil = self.perfil.save()
        usuario = super().save()

        return usuario


class ActividadForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
