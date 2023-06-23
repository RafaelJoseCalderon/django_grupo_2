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
from .forms import ActividadSearchBaseForm
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

    if request.user.is_staff:
        return redirect(reverse_lazy('admin:index'))
    
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


class PlanDeVueloMixin:
    form_class = PlanDeVueloForm
    template_name = 'plan-de-vuelo-form.html'

    success_url = reverse_lazy('planes-de-vuelo')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['extra_kwargs'] = self.request.user

        return kwargs


class AltaPlanDeVuelo(PlanDeVueloMixin, InstructorMixin, CreateView):
    permission_required = 'usuarios.add_plandevuelo'
    extra_context = {
        'titulo': 'Alta Plan de Vuelo',
        'boton_from': 'Crear'
    }
    messages_success = 'Se ha creado correctamente'


class ModiPlanDeVuelo(PlanDeVueloMixin, InstructorMixin, UpdateView):
    permission_required = 'usuarios.change_plandevuelo'
    model = PlanDeVuelo
    extra_context = {
        'titulo': 'Actualización Plan de Vuelo',
        'boton_from': 'Actualizar'
    }
    messages_success = 'Se ha actualizado correctamente'


class BajaPlanDeVuelo(InstructorMixin, DeleteView):
    permission_required = 'usuarios.delete_plandevuelo'

    model = PlanDeVuelo
    template_name = 'componentes/confirmacion_borrado.html'

    success_url = reverse_lazy('planes-de-vuelo')
    extra_context = {'cancel_url': 'planes-de-vuelo'}


# %                          Actividades                                  %
class ActividadesInstructor(InstructorMixin, ListViewWSAP):
    permission_required = 'usuarios.view_actividad'

    model = Actividad
    template_name = 'actividades.html'
    context_object_name = 'actividades'

    paginate_by = 4
    ordering = 'id'

    class_form = ActividadSearchForm
    search_dict = {
        'piloto': 'piloto__first_name__contains',
        'fecha_desde': 'plan_de_vuelo__fecha__gte',
        'fecha_hasta': 'plan_de_vuelo__fecha__lte'
    }

    def get_queryset(self):
        usuario = self.request.user
        self.queryset = Actividad.objects.filter(plan_de_vuelo__instructor = usuario.pk)

        return super().get_queryset()


class DetalleActividad(InstructorMixin, DetailView):
    permission_required = 'usuarios.view_actividad'

    model = Actividad
    template_name = 'actividad.html'

class ActvidadMixin:
    form_class = ActividadForm
    template_name = 'actividad-form.html'

    success_url = reverse_lazy('actividades-i')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['extra_kwargs'] = self.request.user

        return kwargs


class AltaActvidad(ActvidadMixin, InstructorMixin, CreateView):
    permission_required = 'usuarios.add_actividad'
    extra_context = {
        'titulo': 'Alta Actividad',
        'boton_from': 'Crear'
    }


class ModiActvidad(ActvidadMixin, InstructorMixin, UpdateView):
    permission_required = 'usuarios.change_actividad'
    model = Actividad
    extra_context = {
        'titulo': 'Actualización Actividad',
        'boton_from': 'Actualizar'
    }


class BajaActvidad(InstructorMixin, DeleteView):
    permission_required = 'usuarios.delete_actividad'

    model = Actividad
    template_name = 'componentes/confirmacion_borrado.html'

    success_url = reverse_lazy('actividades-i')
    extra_context = {'cancel_url': 'actividades-i'}


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %                            Seccion Piloto                             %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class PilotoMixin(
    PermissionRequiredMixin,
    LoginRequiredMixin
):
    pass


class ActividadesPiloto(PilotoMixin, ListViewWSAP):
    permission_required = 'usuarios.view_actividad'

    model = Actividad
    template_name = 'actividades.html'
    context_object_name = 'actividades'

    paginate_by = 4
    ordering = 'id'

    class_form = ActividadSearchBaseForm
    search_dict = {
        'fecha_desde': 'plan_de_vuelo__fecha__gte',
        'fecha_hasta': 'plan_de_vuelo__fecha__lte'
    }

    def get_queryset(self):
        usuario = self.request.user
        self.queryset = Actividad.objects.filter(piloto = usuario.pk)

        return super().get_queryset()
