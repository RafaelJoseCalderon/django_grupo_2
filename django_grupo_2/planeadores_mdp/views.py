from django.shortcuts import render
from .forms import ContactoForm

def home(request):
    context = {}
    return render(request, 'home.html', context)

def aeronaves(request):
    context = {}
    return render(request, 'aeronaves.html', context)

def institucion(request):
    context = {}
    return render(request, 'institucion.html', context)

# def preguntasFrecuentes(request):
#     context = {}
#     return render(request, 'preguntas_frecuentes.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        print("o envio por correo")
        print("o lo guardo en bbdd para administrarlo en otra vista")
        print("la validacion la debo")
    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})

def only_socios(request):
    context = {}
    return render(request, 'only_socios.html', context)
