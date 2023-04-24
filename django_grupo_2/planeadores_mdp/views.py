from django.shortcuts import render

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
    context = {}
    return render(request, 'contacto.html', context)

def only_socios(request):
    context = {}
    return render(request, 'only_socios.html', context)