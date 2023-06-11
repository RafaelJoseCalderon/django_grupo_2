from django.db import migrations, models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from ..models import Instructor, Piloto, Planeador, Remolcador


def setUp(apps, scheme_editor):
    """Remolcador"""
    remolcadores = []

    remolcadores.append(
        Remolcador.objects.create(
            nombre = 'robin-aircraft DR401 - 180R',
            carga_util_maxima = 1000,
            tanque_combustible = 160,
            velociad_crucero = 123,
            velocidad_maxima = 124,
            autonomia_de_vuelo = 944,
            contras_de_combustible = 39.0,
            tasa_de_ascenso = 770,
            maxima_altura = 20000,
            imagen = "remolcadores/dr401_180r.jpg"
        )
    )

    remolcadores.append(
        Remolcador.objects.create(
            nombre = 'robin-aircraft DR401 - 155R',
            carga_util_maxima = 920,
            tanque_combustible = 160,
            velociad_crucero = 122,
            velocidad_maxima = 132,
            autonomia_de_vuelo = 1507,
            contras_de_combustible = 23.8,
            tasa_de_ascenso = 650,
            maxima_altura = 16000,
            imagen = "remolcadores/dr401_155r.jpg"
        )
    )

    for remolcador in remolcadores:
        remolcador.save()

    """ Planeadores """
    planeadores = []

    planeadores.append(
        Planeador.objects.create(
            nombre = 'JS2 Revelation',
            envergadura = 18,
            area_del_ala = 11.19,
            relacion_de_aspecto = 28.8,
            peso_maximo = 640,
            peso_minimo = 400,
            imagen = "planeadores/js2_revelation.jpg"
        )
    )

    planeadores.append(
        Planeador.objects.create(
            nombre = 'JS3 Rapture',
            envergadura = 18,
            area_del_ala = 9.95,
            relacion_de_aspecto = 32.8,
            peso_maximo = 600,
            peso_minimo = 296,
            imagen = "planeadores/js3_rapture.jpg"
        )
    )

    planeadores.append(
        Planeador.objects.create(
            nombre = 'JS4 Rengeti',
            envergadura = 18,
            area_del_ala = 11.25,
            relacion_de_aspecto = 28.8,
            peso_maximo = 600,
            peso_minimo = 291,
            imagen = "planeadores/js4_rengeti.jpg"
        )
    )

    planeadores.append(
        Planeador.objects.create(
            nombre = 'AS 35 Mi',
            envergadura = 20,
            area_del_ala = 11.75,
            relacion_de_aspecto = 34,
            peso_maximo = 730,
            peso_minimo = 455,
            imagen = "planeadores/as_35_mi.jpg"
        )
    )

    planeadores.append(
        Planeador.objects.create(
            nombre = 'ASH 31 Mi',
            envergadura = 21,
            area_del_ala = 13.20,
            relacion_de_aspecto = 33.5,
            peso_maximo = 700,
            peso_minimo = 455,
            imagen = "planeadores/ash_31_mi.jpg"
        )
    )

    for planeador in planeadores:
        planeador.save()

    """ Root """
    root = User(
        username = 'root',
        first_name = 'root',
        last_name = 'root',
        email = 'root@root.com',
        is_superuser = True,
        is_staff = True,
        is_active = True,
    )
    
    root.set_password('root')
    root.save()

    """Usuarios Grupos"""
    grupos = []

    grupos.append(
        Group.objects.create(
            name='Instructores'
        )
    )

    grupos.append(
        Group.objects.create(
            name='Pilotos'
        )
    )

    for grupo in grupos:
        grupo.save()

    """Usuarios Usuarios"""
    usuarios = []

    usuarios.append(
        Instructor.objects.create(
            username = 'adan',
            first_name = 'Adan',
            last_name = 'AdanAdan',
            email = 'Adan@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 48295602
        )
    )

    usuarios.append(
        Instructor.objects.create(
            username = 'eva',
            first_name = 'Eva',
            last_name = 'EvaEva',
            email = 'EvaEva@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 74244764
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'bonifacio',
            first_name = 'Bonifacio',
            last_name = 'Gomez',
            email = 'bonifacio@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 62899927
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'clemente',
            first_name = 'Clemente',
            last_name = 'Lopez',
            email = 'clemente@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 34941794
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'dalmacio',
            first_name = 'Dalmacio',
            last_name = 'Martinez',
            email = 'dalmacio@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 89208350
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'emeterio',
            first_name = 'Emeterio',
            last_name = 'Garcia',
            email = 'emeterio@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 95659876
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'taciana',
            first_name = 'Taciana',
            last_name = 'Moyano',
            email = 'taciana@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 31650108
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'ursula',
            first_name = 'Ursula',
            last_name = 'Campos',
            email = 'ursula@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 38923477
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'valentina',
            first_name = 'Valentina',
            last_name = 'Soto',
            email = 'valentina@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 52480511
        )
    )

    usuarios.append(
        Piloto.objects.create(
            username = 'zeferina',
            first_name = 'Zeferina',
            last_name = 'Chávez',
            email = 'zeferina@email.com',
            is_superuser = False,
            is_staff = False,
            is_active = True,
            dni = 75797068
        )
    )

    for usuario in usuarios:
        usuario.set_password('1234')
        usuario.save()


class Migration(migrations.Migration):
    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(setUp),
    ]
