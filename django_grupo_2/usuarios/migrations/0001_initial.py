# Generated by Django 4.2 on 2023-05-30 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo electronico')),
                ('dni', models.BigIntegerField(verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructores',
            },
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo electronico')),
                ('dni', models.BigIntegerField(verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'Piloto',
                'verbose_name_plural': 'Pilotos',
            },
        ),
        migrations.CreateModel(
            name='Planeador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('envergadura', models.IntegerField(verbose_name='Envergadura')),
                ('area_del_ala', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Area del ala')),
                ('relacion_de_aspecto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Relacion de aspecto')),
                ('peso_maximo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Peso maximo')),
                ('peso_minimo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Peso minimo')),
                ('imagen', models.ImageField(upload_to='planeadores', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Planeador',
                'verbose_name_plural': 'Planeadores',
            },
        ),
        migrations.CreateModel(
            name='Remolcador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('carga_util_maxima', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Carga util maxima')),
                ('tanque_combustible', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tanque combustible')),
                ('velociad_crucero', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Velociad crucero')),
                ('velocidad_maxima', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Velociad maxima')),
                ('autonomia_de_vuelo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Autonomia de vuelo')),
                ('contras_de_combustible', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Contras de combustible')),
                ('tasa_de_ascenso', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tasa de ascenso')),
                ('maxima_altura', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Maxima altura')),
                ('imagen', models.ImageField(upload_to='remolcadores', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Remolcador',
                'verbose_name_plural': 'Remolcadores',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='seguridad', verbose_name='Imagen')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.instructor')),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.piloto')),
                ('planeador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.planeador')),
                ('remolcador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='usuarios.remolcador')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
    ]
