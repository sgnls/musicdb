from django_enumfield import EnumField

from django.db import models

from musicdb.utils.user_data import PerUserData

class Profile(PerUserData('profile')):
    prefix = models.CharField(
        blank=True,
        max_length=500,
        verbose_name="Override file location prefix",
    )

    kindle_email_address = models.EmailField(blank=True)
