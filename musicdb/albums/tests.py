from musicdb.utils.test import TestCase

class SmokeTests(TestCase):
    def test_view(self):
        self.assertHTTP302('albums:view')
        self.assertHTTP200('albums:view', 'a')
