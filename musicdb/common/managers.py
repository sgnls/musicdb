from django.db import models
from django.core.files import File
from django.core.files.storage import default_storage

class FileManager(models.Manager):
    def create_from_path(self, src, location):
        with open(src) as f:
            assert default_storage.save(location, File(f)) == location

        return self.create(location=location)
