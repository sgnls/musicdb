# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Track'
        db.create_table(u'books_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tracks', to=orm['books.Book'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('file', self.gf('django.db.models.fields.related.OneToOneField')(related_name='audiobook_track', unique=True, to=orm['common.File'])),
        ))
        db.send_create_signal(u'books', ['Track'])

        # Adding unique constraint on 'Track', fields ['book', 'num']
        db.create_unique(u'books_track', ['book_id', 'num'])

    def backwards(self, orm):
        # Removing unique constraint on 'Track', fields ['book', 'num']
        db.delete_unique(u'books_track', ['book_id', 'num'])

        # Deleting model 'Track'
        db.delete_table(u'books_track')

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
            'book': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'mobi_file'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['books.Book']"}),
            'file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'book_mobi'", 'unique': 'True', 'to': u"orm['common.File']"})
        },
        u'books.track': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('book', 'num'),)", 'object_name': 'Track'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': u"orm['books.Book']"}),
            'file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'audiobook_track'", 'unique': 'True', 'to': u"orm['common.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        },
        u'common.file': {
            'Meta': {'object_name': 'File'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['books']