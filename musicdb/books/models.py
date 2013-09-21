from django.db import models

class Author(models.Model):
    last_name = models.CharField(max_length=100)
    first_names = models.CharField(max_length=100)

    class Meta:
        ordering = ('last_name', 'first_names')

    def __unicode__(self):
        return "%s %s" % (self.first_names, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=250)

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

class File(models.Model):
    book = models.ForeignKey(Book, related_name='files')

    file = models.OneToOneField('common.File', related_name='book')
