from django.contrib import messages
from django.utils.safestring import mark_safe


def messages_success(request, message):
    messages.success(request, mark_safe(message))