from django import forms
from django.contrib.auth.forms import UserCreationForm

from .tools import get_singup_user_model


UserSingup = get_singup_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserSingup
        fields = ['username', 'first_name', 'last_name', 'email', 'dni']
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
                }),
            'dni': forms.TextInput(
                attrs = {
                    'placeholder': '99999999'
            })
        }
        help_texts = {
            'first_name': 'Obligatorio. 150 caracteres o menos.',
            'last_name': 'Obligatorio. 150 caracteres o menos.',
            'email': 'Ingresa una dirección de correo electrónico válida',
            'dni': 'Ingresa un numero entero, sin puntos, comas o espacios'
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

        if UserSingup.objects.filter(email = email).exists():
            raise forms.ValidationError('El mail ya esta registrado, prueba con otro')

        return email
