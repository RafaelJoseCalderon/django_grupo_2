from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'home.html', context)

def imagenes(request):
    context = {}
    return render(request, 'imagenes.html', context)

def tarifas(request):
    context = {}
    return render(request, 'tarifas.html', context)

def preguntasFrecuentes(request):
    context = {}
    return render(request, 'preguntas_frecuentes.html', context)

def formularioContacto(request):
    context = {}
    return render(request, 'formulario_contacto.html', context)
