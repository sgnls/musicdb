from django.db import models

class ArtistManager(models.Manager):
    def letters(self):
        return self.values_list(
            'name_first', flat=True,
        ).order_by(
            'name_first',
        ).distinct()

class AlbumManager(models.Manager):
    def get_from_field(self, field, artist_val, val):
        return self.model.objects.get(**{
            field: val,
            'artist__%s' % field: artist_val,
        })

    def get_from_slugs(self, artist_slug, slug):
        return self.get_from_field('slug', artist_slug, slug)

    def get_from_dir_name(self, artist_dir_name, dir_name):
        return self.get_from_field('dir_name', artist_dir_name, dir_name)

class TrackManager(models.Manager):
    def get_from_dir_name(self, dir_name, album):
        return self.model.objects.get(dir_name=dir_name, cd__album=album)
