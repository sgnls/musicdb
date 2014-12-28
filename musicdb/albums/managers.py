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

class TrackManager(models.Manager):
    def total_duration(self):
        return self.aggregate(
            x=models.Sum('music_file__length'),
        )['x'] or 0
