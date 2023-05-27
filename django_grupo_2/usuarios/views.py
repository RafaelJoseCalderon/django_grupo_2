from django.views.generic.list import ListView
from django.views.generic import CreateView

from .forms import ActividadForm
from .models import Actividad


class ActvidadAlta(CreateView):
    template_name = 'alta_actividad.html'
    form_class = ActividadForm
    success_url = 'actividades'


class ListaActividades(ListView):
    template_name = 'lista_actividades.html'
    context_object_name = 'actividades'
    model = Actividad
