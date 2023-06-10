from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'placeholder': 'juan_perez'
                }),
            'first_name': forms.TextInput(
                attrs = {
                    'placeholder': 'juan'
                }),
            'last_name': forms.TextInput(
                attrs = {
                    'placeholder': 'perez'
                }),
            'email': forms.EmailInput(
                attrs = {
                    'placeholder': 'juan_perez@email.com',
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

        self.fields['username'].widget.attrs.pop("autofocus", None)

        self.fields['password1'].widget.attrs['placeholder'] = '******'
        self.fields['password2'].widget.attrs['placeholder'] = '******'

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = True

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('El mail ya esta registrado, prueba con otro')

        return email
