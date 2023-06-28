from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail


class ContactoForm(forms.Form):
    nombre_completo = forms.CharField(
        label = 'Nombre Completo', 
        max_length = 100,
        help_text = 'Por favor ingrese su nombre y apellido completo, los mismos no pueden superar los 100 caracteres',
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

    def send_mail(self):
        data = self.cleaned_data
        send_mail(
            data.get('asunto'),
            f"Nombre Completo: {data.get('nombre_completo')}\n" + 
            f"Mensaje: {data.get('mensaje')}",
            data.get('correo_electronico'),
            ["wololo@secretaria.com"],
            fail_silently=False
        )
