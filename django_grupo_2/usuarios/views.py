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
from herramientas.views import ListViewWithSearchAndPagination

from .forms import UsuarioPerfilForm
from .forms import PlanDeVueloForm
from .forms import ActividadForm
from .forms import PlanDeVueloSearchForm
from .forms import ActividadSearchForm

from .models import Perfil
from .models import Actividad
from .models import PlanDeVuelo


def redireccion(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    if request.user.groups.filter(name='Pilotos').exists():
        return redirect(reverse_lazy('actividades-p'))

    if request.user.groups.filter(name='Instructores').exists():
        return redirect(reverse_lazy('planes-de-vuelo'))

    raise Exception('Usuario sin grupo admitido')


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                            Seccion Perfil                             %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
    template_name = 'perfil-actualizacion.html'
    form_class = UsuarioPerfilForm

    success_url = reverse_lazy('editar-perfil')
    messages_success = 'Se ha actualizado correctamente.'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                          Seccion Instructor                           %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class InstructorMixin(MessagesSuccessMixin, LoginRequiredMixin):
    extra_context = { 'es_instructor': True }


class PlanesDeVuelo(InstructorMixin, ListViewWithSearchAndPagination):
    model = PlanDeVuelo
    template_name = 'planes-de-vuelo.html'
    context_object_name = 'planes_de_vuelo'

    paginate_by = 2
    ordering = 'id'

    class_form = PlanDeVueloSearchForm
    search_dict = {
        'denominacion': 'denominacion__contains',
        'fecha': 'fecha'
    }

    def get_queryset(self):
        usuario = self.request.user
        self.queryset = PlanDeVuelo.objects.filter(instructor = usuario.pk)

        return super().get_queryset()


class DetallePlanDeVuelo(InstructorMixin, DetailView):
    model = PlanDeVuelo
    template_name = 'plan-de-vuelo.html'


class AltaPlanDeVuelo(InstructorMixin, CreateView):
    template_name = 'plan-de-vuelo-form.html'
    form_class = PlanDeVueloForm
    success_url = reverse_lazy('alta-plan-de-vuelo')


class BajaPlanDeVuelo(InstructorMixin, DeleteView):
    model = PlanDeVuelo
    success_url = reverse_lazy('alta-plan-de-vuelo')
    template_name = 'componentes/confirmacion_borrado.html'


class ModiPlanDeVuelo(InstructorMixin, UpdateView):
    model = PlanDeVuelo
    template_name = 'plan-de-vuelo-form.html'
    form_class = PlanDeVueloForm
    success_url = reverse_lazy('alta-plan-de-vuelo')
    messages_success = 'Se ha actualizado correctamente.'


class ActividadesInstructor(InstructorMixin, ListViewWithSearchAndPagination):
    model = Actividad
    template_name = 'actividades.html'
    context_object_name = 'actividades'

    paginate_by = 6
    ordering = 'id'

    class_form = ActividadSearchForm
    search_dict = {
        'piloto': 'piloto__first_name__contains'
    }

    def get_queryset(self):
        usuario = self.request.user
        self.queryset = Actividad.objects.filter(plan_de_vuelo__instructor = usuario.pk)

        return super().get_queryset()


class DetalleActividad(InstructorMixin, DetailView):
    model = Actividad
    template_name = 'actividad.html'


class AltaActvidad(InstructorMixin, CreateView):
    template_name = 'actividad-form.html'
    form_class = ActividadForm
    success_url = reverse_lazy('actividades-i')


class BajaActvidad(InstructorMixin, DeleteView):
    model = Actividad
    success_url = reverse_lazy('actividades-i')
    template_name = 'componentes/confirmacion_borrado.html'


class ModiActvidad(InstructorMixin, UpdateView):
    template_name = 'actividad-form.html'
    form_class = ActividadForm
    success_url = reverse_lazy('actividades-i')
    model = Actividad
    messages_success = 'Se ha actualizado correctamente.'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                            Seccion Piloto                             %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class PilotoMixin(LoginRequiredMixin):
    extra_context = { 'es_piloto': True }


class ActividadesPiloto(PilotoMixin, ListView):
    template_name = 'actividades.html'
    context_object_name = 'actividades'
    model = Actividad

    def get_queryset(self):
        usuario = self.request.user
        return Actividad.objects.filter(piloto = usuario.pk)