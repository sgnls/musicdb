from musicdb.utils.test import TestCase

from .models import Artist

class SmokeTests(TestCase):
    def setUp(self):
        super(SmokeTests, self).setUp()

        self.artist = Artist.objects.create(
            name="Test artist",
            slug='test-artist',
        )

        self.album = self.artist.albums.create(
            title="Test album",
            slug='test-album',
        )

        self.cd = self.album.cds.create(num=1)

    def test_view(self):
        self.assertHTTP302('albums:view')
        self.assertHTTP200('albums:view', 'a')

    def test_artist(self):
        self.assertHTTP200(self.artist.get_absolute_url())

    def test_album(self):
        self.assertHTTP200(self.album.get_absolute_url())

    def test_play_album(self):
        self.assertHTTP200('albums:play-album', self.album.pk)

    def test_play_cd(self):
        self.assertHTTP200('albums:play-cd', self.album.pk, self.cd.pk)
