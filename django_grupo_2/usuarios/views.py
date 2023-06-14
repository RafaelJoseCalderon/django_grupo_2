from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect

from herramientas.mixins import MessagesSuccessMixin

from .forms import UsuarioPerfilForm
from .forms import ActividadForm
from .models import Perfil
from .models import Actividad


def redireccion(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    if request.user.groups.filter(name='Pilotos').exists():
        return redirect(reverse_lazy('actividades-p'))

    if request.user.groups.filter(name='Instructores').exists():
        return redirect(reverse_lazy('actividades-i'))

    raise Exception('Usuario sin grupo admitido')


## ------------- Seccion Perfil -------------- ##
class PerfilMixin(MessagesSuccessMixin, LoginRequiredMixin):
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
    success_url = reverse_lazy('editar-perfil')
    messages_success = 'Se ha actualizado correctamente.'


## ------------- Seccion Instructor ---------- ##
class InstructorMixin(MessagesSuccessMixin, LoginRequiredMixin):
    extra_context = { 'es_instructor': True }


class PlanesDeVuelo(InstructorMixin, ListView):
    pass


class ActividadesInstructor(InstructorMixin, ListView):
    template_name = 'actividades.html'
    context_object_name = 'actividades'
    model = Actividad


class AltaActvidad(InstructorMixin, CreateView):
    template_name = 'actividad.html'
    form_class = ActividadForm
    success_url = reverse_lazy('actividades-i')


class BajaActvidad(InstructorMixin, DeleteView):
    model = Actividad
    success_url = reverse_lazy('actividades-i')
    template_name = 'componentes/confirmacion_borrado.html'


class ModiActvidad(InstructorMixin, UpdateView):
    template_name = 'actividad.html'
    form_class = ActividadForm
    success_url = reverse_lazy('actividades-i')
    model = Actividad
    messages_success = 'Se ha actualizado correctamente.'


## ------------- Seccion Piloto -------------- ##
class PilotoMixin(LoginRequiredMixin):
    extra_context = { 'es_piloto': True }


class ActividadesPiloto(PilotoMixin, ListView):
    template_name = 'actividades.html'
    context_object_name = 'actividades'
    model = Actividad

    def get_queryset(self):
        usuario = self.request.user
        return Actividad.objects.filter(piloto = usuario.pk)