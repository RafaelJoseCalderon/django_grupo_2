from django.urls import path

from .views import SingUp
from .views import PasswordChange
from .views import PasswordReset
from .views import PasswordResetDone
from .views import PasswordResetConfirm


urlpatterns = [
    path(
        route = 'singup/',
        view = SingUp.as_view(),
        name = 'singup'
    ),
    path(
        route = 'password-change/',
        view = PasswordChange.as_view(),
        name = 'password-change'
    ),
    path(
        route = 'password-reset/',
        view = PasswordReset.as_view(),
        name = 'password-reset'
    ),
    path(
        route = 'password-reset/done/',
        view = PasswordResetDone.as_view(),
        name = 'password-reset-done'
    ),
    path(
        route = 'reset/<uidb64>/<token>/',
        view = PasswordResetConfirm.as_view(),
        name = 'password-reset-confirm'
    ),
]
