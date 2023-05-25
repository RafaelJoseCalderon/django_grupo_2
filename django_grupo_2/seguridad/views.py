from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .forms import UserRegistrationForm
from .forms import ProfileUpdateForm
from .models import Profile


class SingUp(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario registrado correctamente.')
        messages.success(self.request, 'Ya puedes identificarte.')

        return super().form_valid(form)


class ProfileMixin:
    def get_object(self):
        return Profile.objects.get_or_create(user = self.request.user)[0]


@method_decorator(login_required, name = 'dispatch')
class DetailProfile(ProfileMixin, DetailView):
    template_name = 'profile/detail-profile.html'
    model = Profile


@method_decorator(login_required, name = 'dispatch')
class UpdateProfile(ProfileMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'profile/update-profile.html'
    success_url = reverse_lazy('profile_edit')
    model = Profile

    def form_valid(self, form):
        messages.success(self.request, 'Se ha actualizado correctamente.')

        return super().form_valid(form)


@method_decorator(login_required, name = 'dispatch')
class PasswordChange(PasswordChangeView):
    template_name = 'password/change_form.html'
    success_url = reverse_lazy('profile_edit')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada correctamente.')

        return super().form_valid(form)


class PasswordReset(PasswordResetView):
    template_name = 'password/reset_form.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'password/reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'password/reset_confirm.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Su contraseña ha sido establecida.')
        messages.success(self.request, 'Ahora puede iniciar sesión.')

        return super().form_valid(form)
