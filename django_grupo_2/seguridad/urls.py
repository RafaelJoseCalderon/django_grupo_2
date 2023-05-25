from django.urls import path

from .views import SingUp
from .views import DetailProfile
from .views import UpdateProfile
from .views import PasswordChange
from .views import PasswordReset
from .views import PasswordResetDone
from .views import PasswordResetConfirm


urlpatterns = [
    path('singup/', SingUp.as_view(), name = 'singup'),

    path('profile/', DetailProfile.as_view(), name = 'profile'),
    path('profile_edit/', UpdateProfile.as_view(), name = 'profile_edit'),

    path('password_change/', PasswordChange.as_view(), name = 'password_change'),
    path('password_reset/', PasswordReset.as_view(), name = 'password_reset'),
    path('password_reset/done/', PasswordResetDone.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name = 'password_reset_confirm'),
]
