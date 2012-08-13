from django_enumfield import EnumField

from django.db import models

from .enums import PlaylistFormatEnum

class Profile(models.Model):
    playlist_format = EnumField(
        PlaylistFormatEnum,
        default=PlaylistFormatEnum.XSPF,
    )

    class Meta:
        managed = False

    def save(self, request):
        data = {}
        for x in self._meta.fields:
            data[x.attname] = x.value_to_string(self)
        request.session['profile'] = data
