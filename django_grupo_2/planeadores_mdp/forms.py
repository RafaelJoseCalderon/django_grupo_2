from django import forms
from django.core.exceptions import ValidationError

class ContactoForm(forms.Form):
    nombre_completo = forms.CharField(
        label = 'Nombre Completo', 
        max_length = 100,
        help_text = 'El nombre es requerido, no puede superar los 100 caracteres',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Juan Perez'
            }
        )
    )

    correo_electronico = forms.EmailField(
        label = 'Email',
        help_text = 'El e-mail es requerido, no puede superar los 100 caracteres',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'juan_perez@email.com',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
            }
        )
    )

    asunto = forms.CharField(
        max_length = 100,
        help_text = 'El asunto es requerido, no puede superar los 100 caracteres',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    mensaje = forms.CharField(
        max_length = 1000,
        help_text = 'El mensaje es requerido, no puede superar los 1000 caracteres',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control contacto-textarea'
            }
        )
    )

    # tener en cuenta que la validacion va en cascada, primero toma las estandar
    # y luego toma las personalizadas
    def clean_nombre_completo(self):
        nombre_completo = self.cleaned_data['nombre_completo']

        print('nombre_completo')
        # raise ValidationError('wololo')

        return nombre_completo


    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data['correo_electronico']

        print('correo_electronico')
        # raise ValidationError('wololo')

        return correo_electronico

    def clean_asunto(self):
        asunto = self.cleaned_data['asunto']

        print('asunto')
        # raise ValidationError('wololo')
        return asunto

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']

        print('mensaje')
        # raise ValidationError('wololo')

        return mensaje
