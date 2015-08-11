from django.core.files import File
from django.core.management.base import BaseCommand

from musicdb.utils.wikipedia_image import get_wikipedia_image

from ...models import Artist

class Command(BaseCommand):
    def handle(self, *files, **options):
        for x in Artist.objects.composers():
            self.handle_artist(x)

    def handle_artist(self, artist):
        f = get_wikipedia_image(artist.short_name())

        if f is None:
            print "W: No image found for %s" % artist
            return

        try:
            artist.image.save(File(f))
        except Exception, exc:
            print "W: Exception when saving for %s: %s" % (artist, exc)

        artist.save()

        print "I: Saved image for %s" % artist
