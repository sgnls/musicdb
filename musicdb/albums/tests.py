from musicdb.utils.test import TestCase

from .models import Artist

class SmokeTests(TestCase):
    def setUp(self):
        super(SmokeTests, self).setUp()

        artist = Artist.objects.create(name="Test artist")
        artist.albums.create(title="Test album")

    def test_view(self):
        self.assertHTTP302('albums:view')
        self.assertHTTP200('albums:view', 'a')

    def test_artist(self):
        artist = Artist.objects.get()

        self.assertHTTP200(artist.get_absolute_url())

    def test_album(self):
        album = Artist.objects.get().albums.get()

        self.assertHTTP200(album.get_absolute_url())
