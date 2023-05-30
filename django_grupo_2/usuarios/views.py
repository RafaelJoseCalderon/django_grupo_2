from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from .forms import ProfileForm
from .models import Profile

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


class ProfileMixin:
    def get_object(self):
        # la bajeza del codigo chancho

        if not Profile.objects.filter(user_ptr=self.request.user.id).exists():
            user = User.objects.get(pk=self.request.user.id)
            try:
                profile = user.profile
            except:
                profile = Profile.objects.create(user_ptr=user)
                profile.save()
                user.save()

        return Profile.objects.get(user_ptr=self.request.user.id)


@method_decorator(login_required, name = 'dispatch')
class DetailProfile(ProfileMixin, DetailView):
    template_name = 'profile/detail-profile.html'
    model = Profile


@method_decorator(login_required, name = 'dispatch')
class UpdateProfile(ProfileMixin, UpdateView):
    form_class = ProfileForm
    template_name = 'profile/update-profile.html'
    success_url = reverse_lazy('profile_edit')

    def form_valid(self, form):
        messages_success(self.request, 'Se ha actualizado correctamente.')

        return super().form_valid(form)


# tools
def messages_success(request, message):
    messages.success(request, mark_safe(message))
