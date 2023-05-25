from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class InitFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.required = True


class UserMetaBaseForm:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    help_texts = {
        'first_name': 'Obligatorio. 150 caracteres o menos.',
        'last_name': 'Obligatorio. 150 caracteres o menos.',
        'email': 'Introduzca una dirección de correo electrónico válida'
    }


class UserRegistrationForm(InitFormsMixin, UserCreationForm):
    class Meta(UserMetaBaseForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.pop("autofocus", None)

        self.fields['password1'].widget.attrs['placeholder'] = '******'
        self.fields['password2'].widget.attrs['placeholder'] = '******'

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('El mail ya esta registrado, prueba con otro')

        return email


class UserUpdateForm(InitFormsMixin, forms.ModelForm):
    class Meta(UserMetaBaseForm):
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                })
        }

    def __init__(self, *args, **kwargs):
        kwargs['instance'] = kwargs['instance'].user
        super().__init__(*args, **kwargs)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = UserUpdateForm(*args, **kwargs)
        self.fields['picture'].widget.template_name = 'components/clearable_file_input.html'
        self.fields['picture'].widget.attrs['class'] = 'form-control'

    def is_valid(self):
        return super().is_valid() and self.user.is_valid()
  
    def save(self):
        user = self.user.save()
        profile = super().save()

        return profile
