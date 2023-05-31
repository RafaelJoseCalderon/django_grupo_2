from django import forms


class ClearableFileInput(forms.ClearableFileInput):
    template_name = 'clearable_file_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        value = context["widget"]["value"]

        if (value):
            context["widget"]["file_name"] = str(value).split("/")[-1]

        return context
