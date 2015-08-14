# -*- coding: utf-8 -*-

import re
import roman
import datetime

from django_yadt import YADTImageField

from django.db import models

from musicdb.db.mixins import Mergeable, NextPreviousMixin
from musicdb.db.fields import MySlugField, DenormalisedCharField

from musicdb.common.models import MusicFile

from .managers import ArtistManager, RecordingManager, MovementManager

class Artist(models.Model, NextPreviousMixin):
    surname = models.CharField(max_length=100)
    forenames = models.CharField(max_length=100, blank=True)

    original_surname = models.CharField(max_length=100, blank=True)
    original_forenames = models.CharField(max_length=100, blank=True)

    slug = MySlugField('slug_name')
    url = models.CharField(max_length=200, blank=True)

    born = models.IntegerField(blank=True, null=True)
    died = models.IntegerField(blank=True, null=True)
    born_question = models.BooleanField(
        "Year of birth uncertain",
        default=False,
    )
    died_question = models.BooleanField(
        'Year of death uncertain',
        default=False,
    )

    nationality = models.ForeignKey(
        'common.Nationality',
        blank=True,
        null=True,
        related_name='classical_artists',
    )

    image = YADTImageField(variants={
        'large': {
            'format': 'jpeg',
        },
    }, cachebust=True, track_exists=True)

    objects = ArtistManager()

    class Meta:
        ordering = ('surname', 'forenames', 'born')

    def __unicode__(self):
        if self.forenames:
            name = "%s, %s" % (self.surname, self.forenames)
        else:
            name = self.surname

        if self.born or self.died:
            name += " (%s)" % self.date_range()

        return name

    @models.permalink
    def get_absolute_url(self):
        return ('classical:artist', (self.slug,))

    def next_composer(self):
        return super(Artist, self).next(works__isnull=False)

    def previous_composer(self):
        return super(Artist, self).previous(works__isnull=False)

    def slug_name(self):
        if self.forenames:
            return "%s %s" % (self.forenames, self.surname)
        return self.surname
    short_name = slug_name

    def long_name(self):
        name = self.short_name()

        if self.original_surname or self.original_forenames:
            name += " (%s %s)" % (
                self.original_forenames,
                self.original_surname,
            )

        if self.born or self.died:
            name += " (%s)" % self.date_range()

        return name

    def date_range(self):
        born = ""
        if self.born:
            born = "%d%s" % (self.born, self.born_question and '?' or '')

        died = ""
        if self.died:
            died = "%d%s" % (self.died, self.died_question and '?' or '')

        return "%s-%s" % (born, died)

    def performances_by_composer(self):
        # FIXME: Move to manager
        return self.performances.order_by(
            'recording__work__composer',
            'recording__work__sort_value',
        )

    def instruments(self):
        return Instrument.objects.filter(
            performances__artist=self,
        ).distinct()

    def biography(self):
        items = []

        if self.works.exists():
            items.append('composer')

        items.extend(self.instruments().values_list('adjective', flat=True))

        if self.nationality:
            nationality = u"%s " % self.nationality.adjective
        else:
            nationality = ""

        if len(items) > 1:
            last = items.pop()
            res = "%s%s and %s" % (nationality, ", ".join(items), last)
        else:
            res = "%s%s" % (nationality, items[0])

        return res.capitalize()

class Ensemble(models.Model, Mergeable):
    name = models.CharField(max_length=150)

    nationality = models.ForeignKey(
        'common.Nationality',
        blank=True,
        null=True,
        related_name='ensembles',
    )

    slug = MySlugField('name')

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('classical:ensemble', (self.slug,))

    def performances_by_composer(self):
        # FIXME: Move to manager
        return self.performances.order_by(
            'recording__work__composer',
            'recording__work__sort_value',
        )

class Work(models.Model, Mergeable, NextPreviousMixin):
    title = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, blank=True)
    composer = models.ForeignKey(Artist, related_name='works')

    # Year & whether year of composition is uncertain
    year = models.IntegerField(blank=True, null=True)
    year_question = models.BooleanField(default=False)

    key = models.ForeignKey('Key', null=True, blank=True, related_name='works')

    slug = MySlugField('slug_name', filter='slug_filter')
    sort_value = DenormalisedCharField('get_sort_value')

    class Meta:
        ordering = ('sort_value',)

    def __unicode__(self):
        return self.pretty_title()

    @models.permalink
    def get_absolute_url(self):
        return ('classical:work', (self.composer.slug, self.slug))

    def next(self):
        return super(Work, self).next(composer=self.composer)

    def previous(self):
        return super(Work, self).previous(composer=self.composer)

    def pretty_title(self, show_year=True):
        extras = [
            ('key', u" in %s"),
            ('nickname', u" «%s»"),
        ]

        ret = self.title
        for attr, format in extras:
            if getattr(self, attr):
                ret += format % getattr(self, attr)

        if self.catalogues.exists():
            ret += u", %s" % ", ".join(str(x) for x in self.catalogues.all())

        if show_year and self.year:
            ret += " (%d%s)" % (self.year, self.year_question and '?' or '')

        return ret

    def slug_name(self):
        return self.pretty_title(show_year=False)
    short_name = slug_name

    def slug_filter(self):
        return type(self).objects.filter(composer=self.composer)

    def get_sort_value(self):
        val = ''

        def zeropad(match):
            return "%04d" % int(match.group(0))

        for cat in self.catalogues.all():
            val += "%02d%s" % (
                cat.catalogue.num, \
                re.sub(r'\d+', zeropad, cat.value),
            )

        val += re.sub(r'\d+', zeropad, self.title)
        val += self.nickname

        return val

class WorkRelationship(models.Model):
    source = models.ForeignKey(Work, related_name='source_relations')
    derived = models.ForeignKey(Work, related_name='derived_relations')
    nature = models.CharField(max_length=13)

    def __unicode__(self):
        return u"%s => %s (%s)" % (self.source, self.derived, self.nature)

    def source_nature(self):
        return {
            'revision': 'newer revision',
        }.get(self.nature, self.nature)

    def derived_nature(self):
        return {
            'revision': 'revision',
        }.get(self.nature, 'source')

class Catalogue(models.Model):
    prefix = models.CharField(max_length=10)
    artist = models.ForeignKey(Artist, related_name='catalogues')
    num = models.IntegerField('Priority')

    class Meta:
        ordering = ('num',)
        unique_together = (
            ('artist', 'num'),
            ('artist', 'prefix'),
        )

    def __unicode__(self):
        return "%s catalogue of %s" % (self.prefix, self.artist)

class WorkCatalogue(models.Model):
    work = models.ForeignKey(Work, related_name='catalogues')
    catalogue = models.ForeignKey(Catalogue, related_name='works')
    value = models.CharField(max_length=10)

    class Meta:
        ordering = ('catalogue__num',)

    def __unicode__(self):
        return "%s %s" % (self.catalogue.prefix, self.value)

class Instrument(models.Model):
    # eg. "Cello"
    noun = models.CharField(max_length=100, unique=True)

    # eg. "Cellist"
    adjective = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('noun',)

    def __unicode__(self):
        return u"%s" % self.noun

class Key(models.Model):
    # TODO: Move to enumeration

    name = models.CharField(max_length=13)
    minor = models.BooleanField(default=False)

    class Meta:
        ordering = ('name', 'minor')
        unique_together = (('name', 'minor'),)

    def __unicode__(self):
        if self.minor:
            return u"%s minor" % self.name

        return u"%s" % self.name

# Recording-specific

class Recording(models.Model):
    work = models.ForeignKey(Work, related_name='recordings')
    year = models.IntegerField(blank=True, null=True)

    slug = MySlugField('slug_name', filter='slug_filter')

    created = models.DateTimeField(
        default=datetime.datetime.utcnow,
        null=True,
        blank=True,
    )

    objects = RecordingManager()

    def __unicode__(self):
        ret = u"%s" % self.work
        if self.year:
            ret += u" (%d)" % self.year
        return ret

    def delete(self, *args, **kwargs):
        for track in self.get_tracks():
            track.delete()

        super(Recording, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return '%s#%s' % (self.work.get_absolute_url(), self.slug)

    def short_name(self):
        return ", ".join(
            x.get_subclass().short_name() for x in self.performances.all()
        )

    def slug_name(self):
        ret = unicode(self.short_name())
        if self.year:
            ret += " %d" % self.year
        return ret

    def slug_filter(self):
        # FIXME: Move to manager
        return type(self).objects.filter(work=self.work)

    def get_tracks(self):
        return MusicFile.objects.filter(
            movement__recording=self,
        ).order_by('movement')

class Movement(models.Model):
    recording = models.ForeignKey(Recording, related_name='movements')
    title = models.CharField(max_length=300)
    music_file = models.OneToOneField(
        'common.MusicFile',
        related_name='movement',
    )
    section_title = models.CharField(max_length=200, blank=True)
    num = models.IntegerField()

    objects = MovementManager()

    class Meta:
        ordering = ('num',)
        unique_together = ('recording', 'num')

    def __unicode__(self):
        return u"%s" % self.title

    def metadata(self):
        title = self.recording.work.pretty_title(show_year=False)
        if self.recording.movements.count() > 1:
            title += u' - %s. %s' % (roman.toRoman(self.num), self.title)
        title += u' (%s)' % self.recording.short_name()

        return {
            'date': str(self.recording.year) or '',
            'title': title,
            'artist': u"%s" % self.recording.work.composer,
            'genre': 'Classical',
            'tracknumber': str(self.num),
        }

class Performance(models.Model):
    recording = models.ForeignKey(Recording, related_name='performances')
    num = models.IntegerField()
    subclass = models.CharField(max_length=8)

    class Meta:
        unique_together = ('recording', 'num')
        ordering = ('num',)

    def __unicode__(self):
        return u"%s" % self.get_subclass()

    def save(self, *args, **kwargs):
        created = not self.id
        if created:
            self.subclass = {
                'ArtistPerformance': 'artist',
                'EnsemblePerformance': 'ensemble',
            }[type(self).__name__]
        return super(Performance, self).save(*args, **kwargs)

    def get_subclass(self):
        return getattr(self, '%sperformance' % self.subclass)

class ArtistPerformance(Performance):
    artist = models.ForeignKey(
        Artist,
        related_name='performances',
    )

    instrument = models.ForeignKey(
        Instrument,
        related_name='performances',
    )

    class Meta:
        ordering = ('instrument',)

    def __unicode__(self):
        return u"%s performing the %s on %s" % (
            self.artist,
            self.instrument.noun.lower(),
            self.recording,
        )

    def short_name(self):
        return self.artist.surname

class EnsemblePerformance(Performance):
    ensemble = models.ForeignKey(
        Ensemble, related_name='performances',
    )

    def __unicode__(self):
        return u"%s performing on %s" % (self.ensemble, self.recording)

    def short_name(self):
        return self.ensemble.name
