# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('books_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('first_names', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('books', ['Author'])

        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('books', ['Book'])

        # Adding model 'BookAuthor'
        db.create_table('books_bookauthor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='authors', to=orm['books.Book'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='books', to=orm['books.Author'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('books', ['BookAuthor'])

        # Adding unique constraint on 'BookAuthor', fields ['book', 'num']
        db.create_unique('books_bookauthor', ['book_id', 'num'])

        # Adding unique constraint on 'BookAuthor', fields ['book', 'author']
        db.create_unique('books_bookauthor', ['book_id', 'author_id'])

        # Adding model 'File'
        db.create_table('books_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['books.Book'])),
            ('file', self.gf('django.db.models.fields.related.OneToOneField')(related_name='book', unique=True, to=orm['common.File'])),
        ))
        db.send_create_signal('books', ['File'])

    def backwards(self, orm):
        # Removing unique constraint on 'BookAuthor', fields ['book', 'author']
        db.delete_unique('books_bookauthor', ['book_id', 'author_id'])

        # Removing unique constraint on 'BookAuthor', fields ['book', 'num']
        db.delete_unique('books_bookauthor', ['book_id', 'num'])

        # Deleting model 'Author'
        db.delete_table('books_author')

        # Deleting model 'Book'
        db.delete_table('books_book')

        # Deleting model 'BookAuthor'
        db.delete_table('books_bookauthor')

        # Deleting model 'File'
        db.delete_table('books_file')

    models = {
        'books.author': {
            'Meta': {'ordering': "('last_name', 'first_names')", 'object_name': 'Author'},
            'first_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'books.book': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Book'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'books.bookauthor': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('book', 'num'), ('book', 'author'))", 'object_name': 'BookAuthor'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': "orm['books.Author']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authors'", 'to': "orm['books.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        },
        'books.file': {
            'Meta': {'object_name': 'File'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': "orm['books.Book']"}),
            'file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'book'", 'unique': 'True', 'to': "orm['common.File']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'common.file': {
            'Meta': {'object_name': 'File'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['books']