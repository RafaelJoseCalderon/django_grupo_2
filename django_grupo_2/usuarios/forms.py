from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
from .models import Actividad


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'picture']
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                })
        }
        help_texts = {
            'first_name': 'Obligatorio. 150 caracteres o menos.',
            'last_name': 'Obligatorio. 150 caracteres o menos.',
            'email': 'Introduzca una dirección de correo electrónico válida'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = True

        self.fields['picture'].widget.template_name = 'components/clearable_file_input.html'
        self.fields['picture'].required = False


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'
