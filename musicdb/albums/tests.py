from musicdb.utils.test import TestCase

from .models import Artist

class SmokeTests(TestCase):
    def setUp(self):
        super(SmokeTests, self).setUp()

        Artist.objects.create(name="Test artist")

    def test_view(self):
        self.assertHTTP302('albums:view')
        self.assertHTTP200('albums:view', 'a')

    def test_artist(self):
        artist = Artist.objects.get()

        self.assertHTTP200(artist.get_absolute_url())
