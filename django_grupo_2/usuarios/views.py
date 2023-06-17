from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

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
from herramientas.views import ListViewWithSearchAndPagination as ListViewWSAP

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
    model = User
    template_name = 'perfil-detalle.html'


class ActualizacionPerfil(PerfilMixin, UpdateView):
    form_class = UsuarioPerfilForm
    template_name = 'perfil-actualizacion.html'

    success_url = reverse_lazy('editar-perfil')
    messages_success = 'Se ha actualizado correctamente.'

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                          Auxiliar Actividades                         %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Actividades(ListViewWSAP):
    model = Actividad
    template_name = 'actividades.html'
    context_object_name = 'actividades'

    paginate_by = 6
    ordering = 'id'

    class_form = ActividadSearchForm
    search_dict = {
        'piloto': 'piloto__first_name__contains'
    }


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                          Seccion Instructor                           %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class InstructorMixin(
    MessagesSuccessMixin,
    PermissionRequiredMixin,
    LoginRequiredMixin
):
    pass


# %                          PlanesDeVuelo                                %
class PlanesDeVuelo(InstructorMixin, ListViewWSAP):
    permission_required = 'usuarios.view_plandevuelo'

    model = PlanDeVuelo
    template_name = 'planes-de-vuelo.html'
    context_object_name = 'planes_de_vuelo'

    paginate_by = 2
    ordering = 'id'

    class_form = PlanDeVueloSearchForm
    search_dict = {
        'denominacion': 'denominacion__contains',
        'fecha_desde': 'fecha__gte',
        'fecha_hasta': 'fecha__lte'
    }

    def get_queryset(self):
        usuario = self.request.user
        self.queryset = PlanDeVuelo.objects.filter(instructor = usuario.pk)

        return super().get_queryset()


class DetallePlanDeVuelo(InstructorMixin, DetailView):
    permission_required = 'usuarios.view_plandevuelo'

    model = PlanDeVuelo
    template_name = 'plan-de-vuelo.html'


class AltaPlanDeVuelo(InstructorMixin, CreateView):
    permission_required = 'usuarios.add_plandevuelo'

    form_class = PlanDeVueloForm
    template_name = 'plan-de-vuelo-form.html'

    success_url = reverse_lazy('alta-plan-de-vuelo')


class BajaPlanDeVuelo(InstructorMixin, DeleteView):
    permission_required = 'usuarios.delete_plandevuelo'

    model = PlanDeVuelo
    template_name = 'componentes/confirmacion_borrado.html'

    success_url = reverse_lazy('alta-plan-de-vuelo')


class ModiPlanDeVuelo(InstructorMixin, UpdateView):
    permission_required = 'usuarios.change_plandevuelo'

    model = PlanDeVuelo
    form_class = PlanDeVueloForm
    template_name = 'plan-de-vuelo-form.html'

    success_url = reverse_lazy('alta-plan-de-vuelo')
    messages_success = 'Se ha actualizado correctamente.'


# %                          Actividades                                  %
class ActividadesInstructor(InstructorMixin, Actividades):
    permission_required = 'usuarios.view_actividad'

    def get_queryset(self):
        usuario = self.request.user
        self.queryset = Actividad.objects.filter(plan_de_vuelo__instructor = usuario.pk)

        return super().get_queryset()


class DetalleActividad(InstructorMixin, DetailView):
    permission_required = 'usuarios.view_actividad'

    model = Actividad
    template_name = 'actividad.html'


class AltaActvidad(InstructorMixin, CreateView):
    permission_required = 'usuarios.add_actividad'

    template_name = 'actividad-form.html'
    form_class = ActividadForm

    success_url = reverse_lazy('actividades-i')


class BajaActvidad(InstructorMixin, DeleteView):
    permission_required = 'usuarios.delete_actividad'

    model = Actividad
    template_name = 'componentes/confirmacion_borrado.html'

    success_url = reverse_lazy('actividades-i')


class ModiActvidad(InstructorMixin, UpdateView):
    permission_required = 'usuarios.change_actividad'

    model = Actividad
    form_class = ActividadForm
    template_name = 'actividad-form.html'

    success_url = reverse_lazy('actividades-i')
    messages_success = 'Se ha actualizado correctamente.'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                            Seccion Piloto                             %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class PilotoMixin(
    PermissionRequiredMixin,
    LoginRequiredMixin
):
    pass


class ActividadesPiloto(PilotoMixin, Actividades):
    permission_required = 'usuarios.view_actividad'

    def get_queryset(self):
        usuario = self.request.user
        self.queryset = Actividad.objects.filter(piloto = usuario.pk)

        return super().get_queryset()
