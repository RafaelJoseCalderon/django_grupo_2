from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic.list import ListView

from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import redirect

from herramientas.utils import messages_success

from .forms import UsuarioPerfilForm
from .forms import ActividadForm
from .models import Perfil
from .models import Actividad


# redireccion en construccion
def redireccion(request):
    print(request.user)

    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    return redirect(reverse_lazy('home'))


## ------------- Seccion Perfil -------------- ##
class PerfilMixin(LoginRequiredMixin):
    def user_id(self):
        return self.request.user.id

    def get_object(self):
        usuario = User.objects.get(pk=self.user_id())

        if not Perfil.objects.filter(usuario=self.user_id()).exists():
            Perfil.objects.create(usuario=usuario)

        return usuario


class DetallePerfil(PerfilMixin, DetailView):
    template_name = 'perfil-detalle.html'
    model = User


class ActualizacionPerfil(PerfilMixin, UpdateView):
    form_class = UsuarioPerfilForm
    template_name = 'perfil-actualizacion.html'
    success_url = reverse_lazy('editar_perfil')

    def form_valid(self, form):
        messages_success(self.request, 'Se ha actualizado correctamente.')

        return super().form_valid(form)


## ------------- Seccion Instructor ---------- ##
class InstructorMixin(LoginRequiredMixin):
    pass


class ActvidadAlta(InstructorMixin, CreateView):
    template_name = 'alta_actividad.html'
    form_class = ActividadForm
    success_url = 'actividades'


class ListaActividades(InstructorMixin, ListView):
    template_name = 'lista_actividades.html'
    context_object_name = 'actividades'
    model = Actividad


## ------------- Seccion Piloto -------------- ##
class PilotoMixin(LoginRequiredMixin):
    pass
