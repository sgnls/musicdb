from django.db import models

class Author(models.Model):
    last_name = models.CharField(max_length=100)
    first_names = models.CharField(max_length=100)

    class Meta:
        ordering = ('last_name', 'first_names')

    def __unicode__(self):
        return "%s %s" % (self.first_names, self.last_name)

class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books')

    title = models.CharField(max_length=250)

    class Meta:
        ordering = ('author', 'title')

    def __unicode__(self):
        return "%s - %s" % (self.author, self.title)
