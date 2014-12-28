from musicdb.utils.test import TestCase

class SmokeTests(TestCase):
    def test_view(self):
        self.assertHTTP200('classical:view')
