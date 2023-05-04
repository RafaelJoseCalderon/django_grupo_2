from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail

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

        if form.is_valid():
            post = request.POST

            try:
                send_mail(
                    post.get('asunto'),
                    f"Nombre Completo: {post.get('nombre_completo')}\n" + 
                    f"Mensaje: {post.get('mensaje')}",
                    post.get('correo_electronico'),
                    ["wololo@secretaria.com"],
                    fail_silently=False
                )

                return redirect(reverse('contacto') + '?ok')
            except:
                return redirect(reverse('contacto') + '?fail')

    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})

def only_socios(request):
    context = {}
    return render(request, 'only_socios.html', context)
