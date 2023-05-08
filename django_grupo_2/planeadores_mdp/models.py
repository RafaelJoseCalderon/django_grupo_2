from django.db import models

# Create your models here.

# class Categoria(models.Model):
#     nombre = models.CharField(max_length=20)

class Aeronave(models.Model):
    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre'
    )

    capacidad = models.IntegerField()

    motor = models.CharField(
        max_length = 50,
        verbose_name = 'Motor'
    )

    velocidad_crucero = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )

    tanque_combustible = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )

    consumo_por_hora = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )

    autonomia = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )

    peso_maximo = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )

    equipaje = models.DecimalField(
        max_digits = 10,
        decimal_places = 2
    )

    imagen = models.ImageField(
        verbose_name = 'Imagen',
        upload_to = 'aeronaves'
    )