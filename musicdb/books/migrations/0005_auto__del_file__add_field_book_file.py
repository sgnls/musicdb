# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'File'
        db.delete_table('books_file')

        # Adding field 'Book.file'
        db.add_column('books_book', 'file',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=-1, related_name='book', unique=True, to=orm['common.File']),
                      keep_default=False)

    def backwards(self, orm):
        # Adding model 'File'
        db.create_table('books_file', (
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['books.Book'])),
            ('file', self.gf('django.db.models.fields.related.OneToOneField')(related_name='book', unique=True, to=orm['common.File'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('books', ['File'])

        # Deleting field 'Book.file'
        db.delete_column('books_book', 'file_id')

    models = {
        'books.author': {
            'Meta': {'ordering': "('last_name', 'first_names')", 'object_name': 'Author'},
            'first_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name_first': ('django.db.models.fields.TextField', [], {'max_length': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'books.book': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Book'},
            'file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'book'", 'unique': 'True', 'to': "orm['common.File']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'books.bookauthor': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('book', 'num'), ('book', 'author'))", 'object_name': 'BookAuthor'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': "orm['books.Author']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authors'", 'to': "orm['books.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        },
        'common.file': {
            'Meta': {'object_name': 'File'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['books']