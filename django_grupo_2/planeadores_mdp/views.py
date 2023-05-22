from django.contrib import messages

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic import CreateView

from .forms import ContactoForm
from .models import Planeador, Remolcador, Actividad


class Home(TemplateView):
    template_name = 'home.html'


class Planeador(ListView):
    template_name = 'planeadores.html'
    context_object_name = 'aeronaves'
    model = Planeador


class Remolcador(ListView):
    template_name = 'remolcadores.html'
    context_object_name = 'aeronaves'
    model = Remolcador


class Institucion(TemplateView):
    template_name = 'institucion.html'


class Contacto(FormView):
    template_name = 'contacto.html'
    success_url = 'contacto'
    form_class = ContactoForm

    def form_valid(self, form):
        try:
            form.send_mail()
            messages.success(self.request, 'Su mensaje se ha enviado correctamente.')
        except:
            messages.error(self.request, 'Error interno, disculpe las molestias.')

        return super().form_valid(form)



class ActvidadAlta(CreateView):
    template_name = 'alta_actividad.html'
    model = Actividad
    fields = '__all__'
    success_url = '/'


class ListaActividades(ListView):
    template_name = 'lista_actividades.html'
    context_object_name = 'actividades'
    model = Actividad
