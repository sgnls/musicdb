import os
import tempfile

from mutagen import mp3, easyid3, File as MutagenFile

from django.db import models
from django.core.files import File as DjangoFile
from django.core.files.storage import default_storage

from musicdb.db.fields import MySlugField

from .managers import FileManager

class AbstractArtist(models.Model):
    slug = MySlugField('slug_name')
    url = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = True

class Nationality(models.Model):
    noun = models.CharField(
        help_text="For example, 'England'",
        max_length=50,
    )

    adjective = models.CharField(
        help_text="For example, 'English'",
        max_length=50,
    )

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
    tags_dirty = models.NullBooleanField(
       'File metadata is out of sync',
        default=True,
    )

    def __unicode__(self):
        return "Length %ds (from %s)" % (self.length, self.file)

    def delete(self, *args, **kwargs):
        super(MusicFile, self).delete(*args, **kwargs)

        self.file.delete()

    def get_parent_instance(self):
        return getattr(self, self.rev_model)

    def tag(self):
        try:
            data = self.get_parent_instance().metadata()

            with tempfile.NamedTemporaryFile(prefix='musicdb') as f:
                # Download
                with default_storage.open(self.file.location) as g:
                    f.write(g.read())
                    f.flush()

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
        except:
            self.tags_dirty = None
            self.save()
            raise
        finally:
            self.tags_dirty = False
            self.save()
