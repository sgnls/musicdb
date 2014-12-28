# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
    def backwards(self, orm):
        pass

    models = {
        'albums.album': {
            'Meta': {'ordering': "('year', 'title')", 'object_name': 'Album', 'db_table': "'nonclassical_album'"},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['albums.Artist']"}),
            'cover': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'null': 'True'}),
            'dir_name': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'albums.artist': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Artist', 'db_table': "'nonclassical_artist'"},
            'dir_name': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_solo_artist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name_first': ('django.db.models.fields.TextField', [], {'max_length': '1', 'db_index': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'albums_artists'", 'null': 'True', 'to': "orm['common.Nationality']"}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'albums.cd': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('album', 'num'),)", 'object_name': 'CD', 'db_table': "'nonclassical_cd'"},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cds'", 'to': "orm['albums.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        },
        'albums.track': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('cd', 'num'),)", 'object_name': 'Track', 'db_table': "'nonclassical_track'"},
            'cd': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': "orm['albums.CD']"}),
            'dir_name': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'track'", 'unique': 'True', 'to': "orm['common.MusicFile']"}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'common.file': {
            'Meta': {'object_name': 'File'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'common.musicfile': {
            'Meta': {'object_name': 'MusicFile'},
            'file': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.File']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rev_model': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'tags_dirty': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'common.nationality': {
            'Meta': {'ordering': "('noun',)", 'object_name': 'Nationality'},
            'adjective': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noun': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['albums']