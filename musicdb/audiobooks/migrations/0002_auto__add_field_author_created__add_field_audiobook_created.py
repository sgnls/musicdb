# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Author.created'
        db.add_column(u'audiobooks_author', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow),
                      keep_default=False)

        # Adding field 'AudioBook.created'
        db.add_column(u'audiobooks_audiobook', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Author.created'
        db.delete_column(u'audiobooks_author', 'created')

        # Deleting field 'AudioBook.created'
        db.delete_column(u'audiobooks_audiobook', 'created')

    models = {
        u'audiobooks.audiobook': {
            'Meta': {'ordering': "('title',)", 'object_name': 'AudioBook'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': u"orm['audiobooks.Author']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'audiobooks.author': {
            'Meta': {'ordering': "('last_name', 'first_names')", 'object_name': 'Author'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'first_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name_first': ('django.db.models.fields.TextField', [], {'max_length': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'audiobooks.track': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('audiobook', 'num'),)", 'object_name': 'Track'},
            'audiobook': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': u"orm['audiobooks.AudioBook']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'audiobook_track'", 'unique': 'True', 'to': u"orm['common.MusicFile']"}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'common.file': {
            'Meta': {'object_name': 'File'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'common.musicfile': {
            'Meta': {'object_name': 'MusicFile'},
            'file': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.File']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rev_model': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['audiobooks']