from musicdb.utils.test import TestCase

class SmokeTests(TestCase):
    def test_landing(self):
        self.assertHTTP200('static:landing')
