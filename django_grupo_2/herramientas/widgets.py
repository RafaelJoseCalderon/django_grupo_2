from django import forms


class ClearableFileInput(forms.ClearableFileInput):
    template_name = 'clearable_file_input.html'
        