from django_yadt import YADTImageField

from django.db import models

from musicdb.db.fields import FirstLetterField, MySlugField

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
        return "%s, %s" % (self.last_name, self.first_names)

    @models.permalink
    def get_absolute_url(self):
        return 'books:author', (self.slug,)

    def long_name(self):
        return "%s %s" % (self.first_names, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=250)

    image = YADTImageField(variants={
        'large': {
            'width': 300,
            'height': 428,
            'format': 'jpeg',
            'fallback': True,
        },
        'thumbnail': {
            'width': 150,
            'height': 213,
            'format': 'jpeg',
            'fallback': True,
        },
    }, cachebust=True)

    file = models.OneToOneField('common.File', related_name='book')

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, related_name='authors')
    author = models.ForeignKey(Author, related_name='books')
    num = models.IntegerField()

    class Meta:
        ordering = ('num',)
        unique_together = (
            ('book', 'num'),
            ('book', 'author'),
        )
