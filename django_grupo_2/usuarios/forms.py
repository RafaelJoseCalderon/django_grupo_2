from django import forms
from django.contrib.auth.models import User

from herramientas.forms import ParentWithChildrenForm
from herramientas.widgets import ClearableFileInput

from .models import Perfil
from .models import Actividad
from .models import PlanDeVuelo


class InitFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                            Seccion Perfil                             %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class PerfilForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen']
        widgets = {
            'imagen': ClearableFileInput()
        }


class UsuarioForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                })
        }


class UsuarioPerfilForm(ParentWithChildrenForm):
    structure = {
        'parent': UsuarioForm,
        'childrens': [
            {'children': PerfilForm, 'related_name': 'perfil'}
        ]
    }


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                        Seccion Plan De Vuel                           %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class PlanDeVueloSearchForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = PlanDeVuelo
        fields = ['denominacion', 'fecha']
        widgets = {
            'fecha': forms.DateInput(
                attrs = {
                    'placeholder': 'AAAA-mm-dd'
            })            
        }

    def __init__(self, *args, **kwargs):
        super(PlanDeVueloSearchForm, self).__init__(*args, **kwargs)

        for value in self.fields.values():
            value.required = False


class PlanDeVueloForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                          Seccion Actividad                            %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class ActividadSearchForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['piloto']

    def __init__(self, *args, **kwargs):
        super(ActividadSearchForm, self).__init__(*args, **kwargs)

        for value in self.fields.values():
            value.required = False


class ActividadForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
