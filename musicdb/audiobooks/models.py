from django_yadt import YADTImageField

from django.db import models

from musicdb.db.fields import FirstLetterField, MySlugField

from musicdb.common.models import MusicFile

from .managers import AuthorManager

class Author(models.Model):
    last_name = models.CharField(max_length=100)
    first_names = models.CharField(max_length=100)

    slug = MySlugField('long_name')
    last_name_first = FirstLetterField('last_name')

    objects = AuthorManager()

    class Meta:
        ordering = ('last_name', 'first_names')

    def __unicode__(self):
        return u"%s, %s" % (self.last_name, self.first_names)

    @models.permalink
    def get_absolute_url(self):
        return 'audiobooks:author', (self.slug,)

    def long_name(self):
        return "%s %s" % (self.first_names, self.last_name)

class AudioBook(models.Model):
    title = models.CharField(max_length=250)

    author = models.ForeignKey(Author, related_name='books')

    image = YADTImageField(variants={
        'large': {
            'format': 'jpeg',
            'pipeline': (
                {'name': 'thumbnail', 'width': 300, 'height': 428},
            ),
        },
        'thumbnail': {
            'format': 'jpeg',
            'pipeline': (
                {'name': 'thumbnail', 'width': 150, 'height': 213},
            ),
        },
    }, track_exists=True, cachebust=True)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return u"%s" % self.title

    def get_tracks(self):
        return MusicFile.objects.filter(
            audiobook_track__audiobook=self,
        ).order_by('audiobook_track__num')

class Track(models.Model):
    title = models.CharField(max_length=250)

    num = models.IntegerField()
    audiobook = models.ForeignKey(AudioBook, related_name='tracks')

    music_file = models.OneToOneField(MusicFile, related_name='audiobook_track')

    class Meta:
        ordering = ('num',)
        unique_together = (
            ('audiobook', 'num'),
        )

    def metadata(self):
        return {
            'title': u"%s" % self.title,
            'album': u"%s" % self.audiobook.title,
            'artist': u"%s" % self.audiobook.author.long_name(),
            'tracknumber': "%d" % self.num,
        }
