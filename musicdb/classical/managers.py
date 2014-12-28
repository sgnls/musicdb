from django.db import models

class ArtistManager(models.Manager):
    def composers(self):
        return self.filter(works__isnull=False).distinct()

    def artists(self):
        return self.filter(performances__isnull=False).distinct()

    def by_num_works(self):
        return self.composers().annotate(
            num_works=models.Count('works'),
        ).order_by('-num_works')

class RecordingManager(models.Manager):
    def recent(self):
        return self.filter(created__isnull=False).order_by('-created')

class MovementManager(models.Manager):
    def total_duration(self):
        return self.aggregate(
            x=models.Sum('music_file__length'),
        )['x'] or 0
