from django.db import migrations
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.sql import emit_post_migrate_signal

from ..models import *


def set_up(apps, schema_editor):
    emit_post_migrate_signal(2, False, 'default')

    plandevuelo_ct = ContentType.objects.get_for_model(PlanDeVuelo)
    plandevuelo_pr = Permission.objects.all().filter(content_type=plandevuelo_ct)

    actividad_ct = ContentType.objects.get_for_model(Actividad)
    actividad_pr = Permission.objects.filter(content_type=actividad_ct)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Instructos                                                            %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    instructor_group = Group.objects.get(name='Instructores')

    for permission in plandevuelo_pr:
        instructor_group.permissions.add(permission)

    for permission in actividad_pr:
        instructor_group.permissions.add(permission)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Piloto                                                                %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    piloto_group = Group.objects.get(name='Pilotos')

    for permission in actividad_pr:
        if permission.codename == "view_actividad":
            piloto_group.permissions.add(permission)


class Migration(migrations.Migration):
    dependencies = [
        ('usuarios', 'init_database'),
    ]

    operations = [
        migrations.RunPython(set_up),
    ]
