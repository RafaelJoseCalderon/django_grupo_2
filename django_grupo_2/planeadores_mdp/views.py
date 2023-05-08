from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactoForm
from .tools import contact_send_mail
from .models import Aeronave

def home(request):
    context = {}
    return render(request, 'home.html', context)

def aeronaves(request):
    aeronaves = Aeronave.objects.all()

    return render(request, 'aeronaves.html', {'aeronaves': aeronaves})


def institucion(request):
    context = {}
    return render(request, 'institucion.html', context)

# def preguntasFrecuentes(request):
#     context = {}
#     return render(request, 'preguntas_frecuentes.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)

        if form.is_valid():
            try:
                contact_send_mail(request)
                form = ContactoForm()
                messages.success(request, 'Su mensaje se ha enviado correctamente.')
            except:
                messages.error(request, 'Error interno, disculpe las molestias.')
    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})

def only_socios(request):
    context = {}
    return render(request, 'only_socios.html', context)
