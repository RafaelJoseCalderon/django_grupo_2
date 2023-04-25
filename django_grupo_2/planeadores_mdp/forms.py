from django import forms


class ContactoForm(forms.Form):
    nombre_completo = forms.CharField(
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Juan Perez'
            }
        )
    )

    correo_electronico = forms.EmailField(
        label = 'Email',
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'juan_perez@email.com',
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
            }
        )
    )

    asunto = forms.CharField(
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    mensaje = forms.CharField(
        max_length = 1000,
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control contacto-textarea'
            }
        )
    )