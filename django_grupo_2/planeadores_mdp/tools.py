from django.core.mail import send_mail


def contact_send_mail(request):
    post = request.POST
    send_mail(
        post.get('asunto'),
        f"Nombre Completo: {post.get('nombre_completo')}\n" + 
        f"Mensaje: {post.get('mensaje')}",
        post.get('correo_electronico'),
        ["wololo@secretaria.com"],
        fail_silently=False
    )