from musicdb.common.models import MusicFile

class Dummy(object):
    pass

class Track(MusicFile):
    length = 0

    def __init__(self, path):
        self.path = path

    def get_parent_instance(self):
        x = Dummy()
        x.title = ''

        return x

    @property
    def file(self):
        x = Dummy()
        x.location = self.path

        return x
