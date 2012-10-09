from django_enumfield import EnumField

from django.db import models

from .enums import PlaylistFormatEnum

class Profile(models.Model):
    playlist_format = EnumField(
        PlaylistFormatEnum,
        default=PlaylistFormatEnum.XSPF,
    )

    prefix = models.CharField(
        blank=True,
        max_length=500,
        verbose_name="Override file location prefix",
    )

    class Meta:
        managed = False

    def save(self, request):
        data = {}
        for x in self._meta.fields:
            data[x.attname] = x.value_to_string(self)
        request.session['profile'] = data
