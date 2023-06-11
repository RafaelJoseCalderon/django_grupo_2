from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


## ------------- Seccion Perfil -------------- ##
class Perfil(models.Model):
    imagen = models.ImageField(
        verbose_name = _('Imagen'),
        upload_to = 'seguridad',
        null = True,
        blank = True
    )

    usuario = models.OneToOneField(
        related_name='perfil',
        to = User,
        on_delete = models.CASCADE
    )

    def save(self, *args, **kwargs):
        try:
            perfil_query = Perfil.objects.filter(id = self.id)

            if perfil_query.exists():
                if perfil_query[0].imagen != self.imagen:
                    perfil_query[0].imagen.delete(save = False)

        except ValueError:
            raise ValueError('Houston, tenemos un problema')

        super(Perfil, self).save(*args, **kwargs)


## ------------- Seccion Usuarios ------------ ##
class Usuario(User):
    class Meta:
        abstract = True

    dni = models.BigIntegerField(
        verbose_name = 'DNI'
    )

    def groups_name(self):
        return ''

    def save(self, *args, **kwargs):
        super(Usuario, self).save(*args, **kwargs)

        try:
            if not self.groups.all():
                self.groups.add(
                    Group.objects.get(name = self.groups_name())
                )

        except ValueError:
            raise ValueError('Houston, tenemos un problema')


class Instructor(Usuario):
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'

    def groups_name(self):
        return 'Instructores'


class Piloto(Usuario):
    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'

    def groups_name(self):
        return 'Pilotos'


## ------------- Seccion Aeronaves ----------- ##
class Remolcador(models.Model):
    class Meta:
        verbose_name = 'Remolcador'
        verbose_name_plural = 'Remolcadores'

    nombre = models.CharField(
        verbose_name = 'Nombre',
        max_length = 50
    )

    carga_util_maxima = models.DecimalField(
        verbose_name = 'Carga util maxima',
        max_digits = 10,
        decimal_places = 2
    )

    tanque_combustible = models.DecimalField(
        verbose_name = 'Tanque combustible',
        max_digits = 10,
        decimal_places = 2
    )

    velociad_crucero = models.DecimalField(
        verbose_name = 'Velociad crucero',
        max_digits = 10,
        decimal_places = 2
    )

    velocidad_maxima = models.DecimalField(
        verbose_name = 'Velociad maxima',
        max_digits = 10,
        decimal_places = 2
    )

    autonomia_de_vuelo = models.DecimalField(
        verbose_name = 'Autonomia de vuelo',
        max_digits = 10,
        decimal_places = 2
    )

    contras_de_combustible = models.DecimalField(
        verbose_name = 'Contras de combustible',
        max_digits = 10,
        decimal_places = 2
    )

    tasa_de_ascenso = models.DecimalField(
        verbose_name = 'Tasa de ascenso',
        max_digits = 10,
        decimal_places = 2
    )

    maxima_altura = models.DecimalField(
        verbose_name = 'Maxima altura',
        max_digits = 10,
        decimal_places = 2
    )

    imagen = models.ImageField(
        verbose_name = 'Imagen',
        upload_to = 'remolcadores'
    )


class Planeador(models.Model):
    class Meta:
        verbose_name = 'Planeador'
        verbose_name_plural = 'Planeadores'

    nombre = models.CharField(
        verbose_name = 'Nombre',
        max_length = 50
    )

    envergadura = models.IntegerField(
        verbose_name = 'Envergadura'
    )

    area_del_ala = models.DecimalField(
        verbose_name = 'Area del ala',
        max_digits = 10,
        decimal_places = 2
    )

    relacion_de_aspecto = models.DecimalField(
        verbose_name = 'Relacion de aspecto',
        max_digits = 10,
        decimal_places = 2
    )

    peso_maximo = models.DecimalField(
        verbose_name = 'Peso maximo',
        max_digits = 10,
        decimal_places = 2
    )

    peso_minimo = models.DecimalField(
        verbose_name = 'Peso minimo',
        max_digits = 10,
        decimal_places = 2
    )

    imagen = models.ImageField(
        verbose_name = 'Imagen',
        upload_to = 'planeadores'
    )


## ------------- Seccion Actividades---------- ##
class Actividad(models.Model):
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.RESTRICT
    )

    piloto = models.ForeignKey(
        Piloto,
        on_delete=models.RESTRICT
    )

    remolcador = models.ForeignKey(
        Remolcador,
        on_delete=models.RESTRICT
    )

    # remolque_despegue = models.TimeField()

    # remolque_corte = models.TimeField()

    planeador = models.ForeignKey(
        Planeador,
        on_delete=models.RESTRICT
    )
