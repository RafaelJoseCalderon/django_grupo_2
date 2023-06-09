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


class FormsDataMixin:
    def get_forms_data(self, kwargs):
        dictionary = dict(kwargs)
        return dictionary, dictionary.pop('extra_kwargs')


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
        widget = widgets.DatePickerInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )

    fecha_hasta = forms.DateField(
        label = 'Fecha Hasta',
        widget = widgets.DatePickerInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )


class PlanDeVueloForm(FormsDataMixin, forms.ModelForm):
    class Meta:
        model = PlanDeVuelo
        fields = '__all__'
        widgets = {
            'denominacion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha': widgets.DatePickerInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'yyyy-mm-dd'
                }
            ),
            # pensando en como no sacar esta cochinada django
            'instructor': forms.HiddenInput(),
            'pilotos_remolcadores': forms.CheckboxSelectMultiple(
                attrs = {
                    'class': 'checkbox-select-multiple'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        dictionary, self.extra_kwargs = self.get_forms_data(kwargs)

        super().__init__(*args, **dictionary)
        self.fields['instructor'].widget.attrs['value'] = self.extra_kwargs.pk

    def clean_instructor(self):
        instructor = self.cleaned_data.get('instructor')

        if instructor.pk != self.extra_kwargs.pk:
            raise forms.ValidationError('mmm, algo malo ha ocurrido')

        return instructor


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                          Seccion Actividad                            %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class ActividadSearchBaseForm(forms.Form):
    fecha_desde = forms.DateField(
        label = 'Fecha Desde',
        widget = widgets.DatePickerInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )

    fecha_hasta = forms.DateField(
        label = 'Fecha Hasta',
        widget = widgets.DatePickerInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'yyyy-mm-dd'
            }
        )
    )


class ActividadSearchForm(ActividadSearchBaseForm):
    field_order = ['piloto',]

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


class ActividadForm(FormsDataMixin, forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
        widgets = {
            'plan_de_vuelo': forms.Select(
                attrs = {'class': 'form-select',}
            ),

            'piloto': forms.Select(
                attrs = {'class': 'form-select',}
            ),

            'remolcador': forms.Select(
                attrs = {'class': 'form-select',}
            ),
            'remolque_despegue': widgets.TimePickerInput(),
            'remolque_corte': widgets.TimePickerInput(),

            'planeador': forms.Select(
                attrs = {'class': 'form-select',}
            ),
            'planeador_aterrizaje': widgets.TimePickerInput(),
            'planeador_vuelo_librado': widgets.TimePickerInput()
        }

    def __init__(self, *args, **kwargs):
        dictionary, self.extra_kwargs = self.get_forms_data(kwargs)
        super().__init__(*args, **dictionary)

        queryset = PlanDeVuelo.objects.filter(instructor = self.extra_kwargs.pk)
        self.fields['plan_de_vuelo'].queryset = queryset