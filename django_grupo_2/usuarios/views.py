from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from herramientas.utils import messages_success

from .forms import UsuarioPerfilForm
from .models import Perfil

from .forms import ActividadForm
from .models import Actividad


class ProfileMixin:
    def user_id(self):
        return self.request.user.id

    def get_object(self):
        usuario = User.objects.get(pk=self.user_id())

        if not Perfil.objects.filter(usuario=self.user_id()).exists():
            Perfil.objects.create(usuario=usuario)

        return usuario


@method_decorator(login_required, name = 'dispatch')
class DetailProfile(ProfileMixin, DetailView):
    template_name = 'perfil-detalle.html'
    model = User


@method_decorator(login_required, name = 'dispatch')
class UpdateProfile(ProfileMixin, UpdateView):
    form_class = UsuarioPerfilForm
    template_name = 'perfil-actualizacion.html'
    success_url = reverse_lazy('profile_edit')

    def form_valid(self, form):
        messages_success(self.request, 'Se ha actualizado correctamente.')

        return super().form_valid(form)


class ActvidadAlta(CreateView):
    template_name = 'alta_actividad.html'
    form_class = ActividadForm
    success_url = 'actividades'


class ListaActividades(ListView):
    template_name = 'lista_actividades.html'
    context_object_name = 'actividades'
    model = Actividad
