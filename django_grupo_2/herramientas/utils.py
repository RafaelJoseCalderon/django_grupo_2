from django.contrib import messages
from django.utils.safestring import mark_safe


def messages_success(request, message):
    messages.success(request, mark_safe(message))

def pop_or_none(data, key):
    value = data.get(key)
    if value: data.pop(key)

    return value