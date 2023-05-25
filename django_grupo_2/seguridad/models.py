from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Profile(models.Model):
    picture = models.ImageField(
        verbose_name = _('Image'),
        upload_to = 'seguridad',
        null = True,
        blank = True
    )

    user = models.OneToOneField(
        to = User,
        on_delete = models.CASCADE
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