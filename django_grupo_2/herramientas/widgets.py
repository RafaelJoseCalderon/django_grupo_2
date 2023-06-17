from django import forms
from .utils import pop_or_none

class ClearableFileInput(forms.ClearableFileInput):
    class Media:
        js = [ 'js/clearable_file_input.js' ]

    template_name = 'clearable_file_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        value = context["widget"]["value"]

        if (value):
            context["widget"]["file_name"] = str(value).split("/")[-1]

        return context


class DateInput(forms.DateInput):
    class Media:
        js = [ 'datepicker-js/js/datepicker.js', 'js/date_input.js' ]
        css = { 'all': ['datepicker-js/css/datepicker.material.css'] }

    template_name = 'date_input.html'

    def __init__(self, *args, **kwargs):
        self.get_widget_data(kwargs)
        super().__init__(*args, **self.widget_data)

    def get_widget_data(self, kwargs):
        self.widget_data = dict(kwargs)

        self.exact = pop_or_none(self.widget_data, 'exact')
        self.min = pop_or_none(self.widget_data, 'min')
        self.max = pop_or_none(self.widget_data, 'max')

        if not self.widget_data.get('attrs'):
            self.widget_data['attrs'] = {}

        if not self.exact:
            if self.min:
                self.widget_data['attrs']['date-picker-min'] = self.min

            if self.max:
                self.widget_data['attrs']['date-picker-max'] = self.max

        return self.widget_data

    def validate(self, value):
        super().validate(value)

        if not self.exact and (self.min > value or self.max < value):
            raise forms.ValidationError('Fecha fuera de rango')
