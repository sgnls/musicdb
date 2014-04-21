from django_enumfield import EnumField

from django.db import models

from musicdb.utils.user_data import PerUserData

from .enums import PlaylistFormatEnum

class Profile(PerUserData('profile')):
    playlist_format = EnumField(
        PlaylistFormatEnum,
        default=PlaylistFormatEnum.XSPF,
    )

    prefix = models.CharField(
        blank=True,
        max_length=500,
        verbose_name="Override file location prefix",
    )

    kindle_email_address = models.EmailField(blank=True)
