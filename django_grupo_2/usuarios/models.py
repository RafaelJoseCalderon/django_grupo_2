from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Profile(User):
    # esto no me anduvo, al crear el perfil me borra el usuario
    # user_ptr = models.OneToOneField(
    #     User,
    #     on_delete=models.PROTECT,
    #     parent_link=True,
    #     primary_key=True,
    # )

    picture = models.ImageField(
        verbose_name = _('Image'),
        upload_to = 'seguridad',
        null = True,
        blank = True
    )

    def save(self, *args, **kwargs):
        try:
            profile_query = Profile.objects.filter(id = self.id)

            if profile_query.exists():
                if profile_query[0].picture != self.picture:
                    profile_query[0].picture.delete(save = False)

        except ValueError:
            raise ValueError('Houston, tenemos un problema')

        super(Profile, self).save(*args, **kwargs)


class Usuario(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre'
    )

    apellido = models.CharField(
        max_length = 50,
        verbose_name = 'Apellido'
    )

    email = models.EmailField(
        max_length = 200,
        verbose_name = 'Correo electronico'
    )

    dni = models.BigIntegerField(
        verbose_name = 'DNI'
    )


class Instructor(Usuario):
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'


class Piloto(Usuario):
    class Meta:
        verbose_name = 'Piloto'
        verbose_name_plural = 'Pilotos'


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
