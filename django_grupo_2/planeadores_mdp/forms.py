from django import forms


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