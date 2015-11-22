# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        from musicdb.books.models import Book, MobiFile

        for x in Book.objects.all():
            MobiFile.objects.create(book=x, file=x.file)

    def backwards(self, orm):
        pass
    models = {
        u'books.author': {
            'Meta': {'ordering': "('last_name', 'first_names')", 'object_name': 'Author'},
            'first_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name_first': ('django.db.models.fields.TextField', [], {'max_length': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'books.book': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Book'},
            'file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'book'", 'unique': 'True', 'to': u"orm['common.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'books.bookauthor': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('book', 'num'), ('book', 'author'))", 'object_name': 'BookAuthor'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': u"orm['books.Author']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authors'", 'to': u"orm['books.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        },
        u'books.mobifile': {
            'Meta': {'object_name': 'MobiFile'},
            'book': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'mobi'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['books.Book']"}),
            'file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'book_mobi'", 'unique': 'True', 'to': u"orm['common.File']"})
        },
        u'common.file': {
            'Meta': {'object_name': 'File'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['books']