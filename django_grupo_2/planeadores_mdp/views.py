from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactoForm
from .tools import contact_send_mail

def home(request):
    context = {}
    return render(request, 'home.html', context)

def aeronaves(request):
    aeronaves = (
        {
            'nombre': 'Piper PA-11 LV-XLT',
            'capacidad': 2,
            'motor': 'Continental 90',
            'velocidad_crucero': 90,
            'tanque_combustible': 64,
            'consumo_por_hora': 20,
            'autonomia': 3.2,
            'peso_maximo': 554,
            'equipaje': 9,
            'imagen': 'media/aeronaves/Piper11.jpg'
        },{
            'nombre': 'Cessna 172 - LV-GRU',
            'capacidad': 4,
            'motor': 'Continental 145',
            'velocidad_crucero': 100,
            'tanque_combustible': 147,
            'consumo_por_hora': 30,
            'autonomia': 4.6,
            'peso_maximo': 1043,
            'equipaje': 22,
            'imagen': 'media/aeronaves/Cessna.jpg'
        },{
            'nombre': 'Aero Boero 180 LV-JZY',
            'capacidad': 4,
            'motor': 'Lycoming 180',
            'velocidad_crucero': 110,
            'tanque_combustible': 64,
            'consumo_por_hora': 20,
            'autonomia': 3.2,
            'peso_maximo': 8444,
            'equipaje': 9,
            'imagen': 'media/aeronaves/AeroBoero.jpg'
        },{
            'nombre': 'Piper PA-28 Cherokee LV-LMC',
            'capacidad': 4,
            'motor': 'Lycoming 180',
            'velocidad_crucero': 100,
            'tanque_combustible': 147,
            'consumo_por_hora': 30,
            'autonomia': 4.6,
            'peso_maximo': 1043,
            'equipaje': 22,
            'imagen': 'media/aeronaves/Piper28.jpg'
        },{
            'nombre': 'Schleicher ASK-13 LV-EAK',
            'capacidad': 4,
            'motor': 'Lycoming 180',
            'velocidad_crucero': 90,
            'tanque_combustible': 64,
            'consumo_por_hora': 20,
            'autonomia': 3.2,
            'peso_maximo': 480,
            'equipaje': 9,
            'imagen': 'media/aeronaves/schleicher.jpg'
        },{
            'nombre': 'Brasov ISD-28',
            'capacidad': 2,
            'motor': 'Lycoming 180',
            'velocidad_crucero': 95,
            'tanque_combustible': 147,
            'consumo_por_hora': 30,
            'autonomia': 4.6,
            'peso_maximo': 590,
            'equipaje': 22,
            'imagen': 'media/aeronaves/Brasov.jpg'
        }
    )

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
