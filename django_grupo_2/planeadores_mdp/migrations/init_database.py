from django.db import migrations, models
from django.contrib.auth.models import User

from ..models import Aeronave


def setUp(apps, scheme_editor):
    """ Aeronaves """
    aeronaves = []

    aeronaves.append(
        Aeronave.objects.create(
            nombre = "Piper PA-11 LV-XLT",
            capacidad = 2,
            motor = "Continental 90",
            velocidad_crucero = 90,
            tanque_combustible = 64,
            consumo_por_hora = 20,
            autonomia = 3.2,
            peso_maximo = 554,
            equipaje = 9,
            imagen = "aeronaves/Piper11.jpg"
        )
    )

    aeronaves.append(
        Aeronave.objects.create(
            nombre = "Cessna 172 - LV-GRU",
            capacidad = 4,
            motor = "Continental 145",
            velocidad_crucero = 100,
            tanque_combustible = 147,
            consumo_por_hora = 30,
            autonomia = 4.6,
            peso_maximo = 1043,
            equipaje = 22,
            imagen = "aeronaves/Cessna.jpg"
        )
    )

    aeronaves.append(
        Aeronave.objects.create(
            nombre = "Aero Boero 180 LV-JZY",
            capacidad = 4,
            motor = "Lycoming 180",
            velocidad_crucero = 110,
            tanque_combustible = 64,
            consumo_por_hora = 20,
            autonomia = 3.2,
            peso_maximo = 8444,
            equipaje = 9,
            imagen = "aeronaves/AeroBoero.jpg"
        )
    )

    aeronaves.append(
        Aeronave.objects.create(
            nombre = "Piper PA-28 Cherokee LV-LMC",
            capacidad = 4,
            motor = "Lycoming 180",
            velocidad_crucero = 100,
            tanque_combustible = 147,
            consumo_por_hora = 30,
            autonomia = 4.6,
            peso_maximo = 1043,
            equipaje = 22,
            imagen = "aeronaves/Piper28.jpg"
        )
    )

    aeronaves.append(
        Aeronave.objects.create(
            nombre = "Schleicher ASK-13 LV-EAK",
            capacidad = 4,
            motor = "Lycoming 180",
            velocidad_crucero = 90,
            tanque_combustible = 64,
            consumo_por_hora = 20,
            autonomia = 3.2,
            peso_maximo = 480,
            equipaje = 9,
            imagen = "aeronaves/schleicher.jpg"
        )
    )

    aeronaves.append(
        Aeronave.objects.create(
            nombre = "Brasov ISD-28",
            capacidad = 2,
            motor = "Lycoming 180",
            velocidad_crucero = 95,
            tanque_combustible = 147,
            consumo_por_hora = 30,
            autonomia = 4.6,
            peso_maximo = 590,
            equipaje = 22,
            imagen = "aeronaves/Brasov.jpg"
        )
    )

    for aeronave in aeronaves:
        aeronave.save()

    """ Usuarios """
    usuarios = []

    usuarios.append(
        User(
            username = 'root',
            first_name = 'root',
            last_name = 'root',
            email = 'root@root.com',
            is_superuser = True,
            is_staff = True,
            is_active = True,
        )
    )
    
    usuarios[0].set_password('root')

    for usuario in usuarios:
        usuario.save()


class Migration(migrations.Migration):
    dependencies = [
        ('planeadores_mdp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(setUp),
    ]
