from django import forms
from django.contrib.auth.models import User

from herramientas.forms import ParentWithChildrenForm
from herramientas import widgets

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
            'imagen': widgets.ClearableFileInput()
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
# %                        Seccion Plan De Vuelo                          %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class PlanDeVueloSearchForm(forms.Form):
    denominacion = forms.CharField(
        label = 'Denominacion', 
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Denominación del plan de vuelo'
            }
        )
    )

    fecha_desde = forms.DateField(
        label = 'Fecha Desde',
        widget = widgets.DateInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )

    fecha_hasta = forms.DateField(
        label = 'Fecha Hasta',
        widget = widgets.DateInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )


class PlanDeVueloForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                          Seccion Actividad                            %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class ActividadSearchBaseForm(forms.Form):
    fecha_desde = forms.DateField(
        label = 'Fecha Desde',
        widget = widgets.DateInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )

    fecha_hasta = forms.DateField(
        label = 'Fecha Hasta',
        widget = widgets.DateInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )


class ActividadSearchForm(ActividadSearchBaseForm):
    piloto = forms.CharField(
        label = 'Piloto', 
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Primer nombre del piloto'
            }
        )
    )


class ActividadForm(InitFormsMixin, forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
