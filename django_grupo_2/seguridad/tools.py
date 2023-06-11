from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# copiado y pegado de get_user_model
def get_singup_user_model():
    try:
        return django_apps.get_model(settings.AUTH_SINGUP_USER_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "AUTH_SINGUP_USER_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed"
            % settings.AUTH_SINGUP_USER_MODEL
        )
