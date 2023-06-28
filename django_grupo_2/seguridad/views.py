from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from herramientas.mixins import MessagesSuccessMixin

from .tools import get_profile_edit_url
from .forms import UserRegistrationForm


class SingUp(MessagesSuccessMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')
    messages_success = 'Usuario registrado correctamente.<br> Ya puedes identificarte.'


class PasswordChange(MessagesSuccessMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'password/change_form.html'
    success_url = reverse_lazy(get_profile_edit_url())
    messages_success = 'Contraseña cambiada correctamente.'
    extra_context = {'profile_edit_url': get_profile_edit_url()}


class PasswordReset(PasswordResetView):
    template_name = 'password/reset_form.html'
    success_url = reverse_lazy('password-reset-done')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'password/reset_done.html'


class PasswordResetConfirm(MessagesSuccessMixin, PasswordResetConfirmView):
    template_name = 'password/reset_confirm.html'
    success_url = reverse_lazy('login')
    messages_success = 'Su contraseña ha sido establecida.<br> Ahora puede iniciar sesión.'
