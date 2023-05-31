from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from herramientas.utils import messages_success

from .forms import UserRegistrationForm


class SingUp(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages_success(self.request,
            'Usuario registrado correctamente.<br> Ya puedes identificarte.'
        )

        return super().form_valid(form)


@method_decorator(login_required, name = 'dispatch')
class PasswordChange(PasswordChangeView):
    template_name = 'password/change_form.html'
    success_url = reverse_lazy('profile_edit')

    def form_valid(self, form):
        messages_success(self.request, 'Contraseña cambiada correctamente.')

        return super().form_valid(form)


class PasswordReset(PasswordResetView):
    template_name = 'password/reset_form.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'password/reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'password/reset_confirm.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages_success(self.request,
            'Su contraseña ha sido establecida.<br> Ahora puede iniciar sesión.'
        )

        return super().form_valid(form)
