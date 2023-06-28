from django.contrib import messages
from django.utils.safestring import mark_safe
from itertools import product


def messages_success(request, message):
    messages.success(request, mark_safe(message))

def pop_or_none(data, key):
    value = data.get(key)
    if value: data.pop(key)

    return value

def minutes_range():
    tuple_ = ()
    for minute in range(0, 60, 5):
        value = '00:' + f'00{minute}'[-2:] + ':00'
        tuple_ += (value, value),

    return tuple_

def time_range():
    hours = []
    for hour in range(0,24):
        hours.append(f'00{hour}'[-2:])

    minutes = []
    for minute in range(0, 60, 15):
        minutes.append(f'00{minute}'[-2:])

    tuple_ = ()
    for prod in product(hours, minutes):
        value = f'{prod[0]}:{prod[1]}:00'
        tuple_ += (value, value),

    return tuple_
