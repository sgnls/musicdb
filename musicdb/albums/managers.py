from django.db import models

class ArtistManager(models.Manager):
    def letters(self):
        return self.values_list(
            'name_first', flat=True,
        ).order_by(
            'name_first',
        ).distinct()

class TrackManager(models.Manager):
    def total_duration(self):
        return self.aggregate(
            x=models.Sum('music_file__length'),
        )['x'] or 0
