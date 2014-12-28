import os
import tempfile

from mutagen import mp3, easyid3, File as MutagenFile

from django.db import models
from django.core.files import File as DjangoFile
from django.core.files.storage import default_storage

from .managers import FileManager

class Nationality(models.Model):
    # eg. "England"
    noun = models.CharField(max_length=50)

    # eg. "English"
    adjective = models.CharField(max_length=50)

    class Meta:
        ordering = ('noun',)
        verbose_name_plural = "Nationalities"

    def __unicode__(self):
        return self.adjective

class File(models.Model):
    location = models.CharField(unique=True, max_length=255)
    size = models.IntegerField("File size in bytes", default=0)

    objects = FileManager()

    def __unicode__(self):
        return "%s (%d bytes)" % (self.location, self.size)

    def url(self):
        return default_storage.url(self.location)

    def delete(self, *args, **kwargs):
        path = self.absolute_location(for_writing=True)

        if os.path.exists(path):
            os.unlink(path)

        super(File, self).delete(*args, **kwargs)

class MusicFile(models.Model):
    file = models.OneToOneField(File)
    length = models.IntegerField("Duration in seconds", default=0)
    rev_model = models.CharField(max_length=8) # track, movement
    type = models.CharField(max_length=4) # mp3, flac

    def __unicode__(self):
        return "Length %ds (from %s)" % (self.length, self.file)

    def delete(self, *args, **kwargs):
        super(MusicFile, self).delete(*args, **kwargs)

        self.file.delete()

    def get_parent_instance(self):
        return getattr(self, self.rev_model)

    def tag(self):
        data = self.get_parent_instance().metadata()

        with tempfile.NamedTemporaryFile(suffix='-musicdb.mp3') as f:
            # Download
            with default_storage.open(self.file.location) as g:
                contents = g.read()

            f.write(contents)
            f.flush()
            f.seek(0)

            audio = MutagenFile(f.name)
            audio.delete()

            if isinstance(audio, mp3.MP3):
                audio.tags = easyid3.EasyID3()

            audio.update(data)
            audio.save()

            self.length = int(audio.info.length)

            # Copy it back
            default_storage.delete(self.file.location)
            dst = default_storage.save(self.file.location, DjangoFile(f))

            assert dst == self.file.location
