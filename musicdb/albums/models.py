import datetime

from django_yadt import YADTImageField

from django.db import models

from musicdb.common.models import MusicFile

from musicdb.db.mixins import NextPreviousMixin
from musicdb.db.fields import MySlugField, FirstLetterField

from .managers import ArtistManager, AlbumManager, TrackManager

class Artist(models.Model, NextPreviousMixin):
    name = models.CharField(max_length=250)

    # Artist represents a single person
    is_solo_artist = models.BooleanField(default=False)

    url = models.CharField(max_length=200, blank=True)
    slug = MySlugField('slug_name')
    name_first = FirstLetterField('name')

    nationality = models.ForeignKey(
        'common.Nationality',
        null=True,
        blank=True,
        related_name='albums_artists',
    )

    objects = ArtistManager()

    class Meta:
        db_table = 'nonclassical_artist'
        ordering = ('name',)

    def __unicode__(self):
        return u"%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return 'albums:artist', (self.slug,)

    def long_name(self):
        if self.is_solo_artist:
            try:
                last, first = self.name.split(', ', 1)
                return "%s %s" % (first, last)
            except ValueError:
                return self.name
        return self.name
    slug_name = long_name

class Album(models.Model, NextPreviousMixin):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, related_name='albums')
    year = models.IntegerField(blank=True, null=True)

    image = YADTImageField(variants={
        'large': {
            'format': 'jpeg',
            'pipeline': (
                {'name': 'crop', 'width': 300, 'height': 300},
            ),
        },
        'thumbnail': {
            'format': 'jpeg',
            'pipeline': (
                {'name': 'crop', 'width': 125, 'height': 125},
            ),
        },
    }, cachebust=True, track_exists=True)

    slug = MySlugField('title')

    created = models.DateTimeField(default=datetime.datetime.utcnow, null=True)

    objects = AlbumManager()

    class Meta:
        ordering = ('year', 'title')
        db_table = 'nonclassical_album'

    def __unicode__(self):
        if self.year:
            return u"%s (%d)" % (self.title, self.year)
        return u"%s" % self.title

    def delete(self, *args, **kwargs):
        for track in self.get_tracks():
            track.delete()

        super(Album, self).delete(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'albums:album', (self.artist.slug, self.slug)

    def get_tracks(self):
        return MusicFile.objects.filter(
            track__cd__album=self,
        ).order_by(
            'track__cd',
            'track',
        )

    def total_duration(self):
        return self.get_tracks().aggregate(
            models.Sum('length'),
        ).values()[0] or 0

    def next(self):
        return super(Album, self).next(artist_id=self.artist_id)

    def previous(self):
        return super(Album, self).previous(artist_id=self.artist_id)

class CD(models.Model):
    album = models.ForeignKey(Album, related_name='cds')
    num = models.IntegerField()

    class Meta:
        ordering = ('num',)
        db_table = 'nonclassical_cd'
        unique_together = ('album', 'num')
        verbose_name_plural = 'CDs'

    def __unicode__(self):
        return u"CD %d of %d from %s" % (
            self.num,
            self.album.cds.count(),
            self.album,
        )

    def get_tracks(self):
        return MusicFile.objects.filter(
            track__cd=self,
        ).order_by(
            'track',
        )

class Track(models.Model):
    title = models.CharField(max_length=250)

    cd = models.ForeignKey(CD, related_name='tracks')
    num = models.IntegerField()

    music_file = models.OneToOneField(
        'common.MusicFile',
        related_name='track',
    )

    objects = TrackManager()

    class Meta:
        ordering = ('num',)
        db_table = 'nonclassical_track'
        unique_together = ('cd', 'num')

    def __unicode__(self):
        return u"%s" % self.title

    def metadata(self):
        album = self.cd.album

        return {
            'title': self.title,
            'album': unicode(album.title),
            'artist': unicode(album.artist.long_name()),
            'tracknumber': str(self.num),
            'date': str(album.year) or '',
        }
