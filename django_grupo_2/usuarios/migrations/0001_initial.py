# Generated by Django 4.2 on 2023-06-12 20:49

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dni', models.BigIntegerField(verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dni', models.BigIntegerField(verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'Piloto',
                'verbose_name_plural': 'Pilotos',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PilotoRemolcador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo electronico')),
                ('dni', models.BigIntegerField(verbose_name='DNI')),
            ],
            options={
                'verbose_name': 'PilotoRemolcador',
                'verbose_name_plural': 'PilotosRemolcadores',
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
            name='PlanDeVuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=50, verbose_name='Denominacion')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='instructor', to='usuarios.instructor')),
                ('pilotos_remolcadores', models.ManyToManyField(related_name='pilotos_remolcadores', to='usuarios.pilotoremolcador')),
            ],
            options={
                'verbose_name': 'PlanDeVuelo',
                'verbose_name_plural': 'PlanesDeVuelo',
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
                ('remolque_despegue', models.TimeField(verbose_name='Despegue Remolcador')),
                ('remolque_corte', models.TimeField(verbose_name='Corte Remolcador')),
                ('planeador_aterrizaje', models.TimeField(verbose_name='Aterrizaje Planeador')),
                ('planeador_vuelo_librado', models.TimeField(verbose_name='Vuelo Librado Planeador')),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='piloto', to='usuarios.piloto')),
                ('plan_de_vuelo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='plan_de_vuelo', to='usuarios.plandevuelo')),
                ('planeador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='planeador', to='usuarios.planeador')),
                ('remolcador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='remolcador', to='usuarios.remolcador')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
    ]
