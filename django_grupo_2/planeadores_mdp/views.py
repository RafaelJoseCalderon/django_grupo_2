from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'home.html', context)

def escuela_de_vuelo(request):
    context = {}
    return render(request, 'escuela_de_vuelo.html', context)

def vuelo_de_bautismo(request):
    context = {}
    return render(request, 'vuelo_de_bautismo.html', context)

def preguntasFrecuentes(request):
    context = {}
    return render(request, 'preguntas_frecuentes.html', context)

def contacto(request):
    context = {}
    return render(request, 'contacto.html', context)

def only_socios(request):
    context = {}
    return render(request, 'only_socios.html', context)