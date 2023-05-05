from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

class Aeronave(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    