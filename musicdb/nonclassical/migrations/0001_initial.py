# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table('nonclassical_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.TextField')(max_length=100, db_index=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('is_solo_artist', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nonclassical_artists', null=True, to=orm['common.Nationality'])),
            ('name_first', self.gf('django.db.models.fields.TextField')(max_length=1, db_index=True)),
            ('dir_name', self.gf('django.db.models.fields.TextField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('nonclassical', ['Artist'])

        # Adding model 'Album'
        db.create_table('nonclassical_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='albums', to=orm['nonclassical.Artist'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cover', self.gf('django.db.models.fields.TextField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.TextField')(max_length=100, db_index=True)),
            ('dir_name', self.gf('django.db.models.fields.TextField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('nonclassical', ['Album'])

        # Adding model 'CD'
        db.create_table('nonclassical_cd', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cds', to=orm['nonclassical.Album'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('nonclassical', ['CD'])

        # Adding unique constraint on 'CD', fields ['album', 'num']
        db.create_unique('nonclassical_cd', ['album_id', 'num'])

        # Adding model 'Track'
        db.create_table('nonclassical_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cd', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tracks', to=orm['nonclassical.CD'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('music_file', self.gf('django.db.models.fields.related.OneToOneField')(related_name='track', unique=True, to=orm['common.MusicFile'])),
            ('dir_name', self.gf('django.db.models.fields.TextField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('nonclassical', ['Track'])

        # Adding unique constraint on 'Track', fields ['cd', 'num']
        db.create_unique('nonclassical_track', ['cd_id', 'num'])

    def backwards(self, orm):
        # Removing unique constraint on 'Track', fields ['cd', 'num']
        db.delete_unique('nonclassical_track', ['cd_id', 'num'])

        # Removing unique constraint on 'CD', fields ['album', 'num']
        db.delete_unique('nonclassical_cd', ['album_id', 'num'])

        # Deleting model 'Artist'
        db.delete_table('nonclassical_artist')

        # Deleting model 'Album'
        db.delete_table('nonclassical_album')

        # Deleting model 'CD'
        db.delete_table('nonclassical_cd')

        # Deleting model 'Track'
        db.delete_table('nonclassical_track')

    models = {
        'common.file': {
            'Meta': {'object_name': 'File'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        },
        'common.musicfile': {
            'Meta': {'object_name': 'MusicFile'},
            'file': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.File']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {}),
            'rev_model': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'tags_dirty': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'common.nationality': {
            'Meta': {'ordering': "('noun',)", 'object_name': 'Nationality'},
            'adjective': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noun': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'nonclassical.album': {
            'Meta': {'ordering': "('year', 'title')", 'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'albums'", 'to': "orm['nonclassical.Artist']"}),
            'cover': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'dir_name': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'nonclassical.artist': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Artist'},
            'dir_name': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_solo_artist': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name_first': ('django.db.models.fields.TextField', [], {'max_length': '1', 'db_index': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nonclassical_artists'", 'null': 'True', 'to': "orm['common.Nationality']"}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'nonclassical.cd': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('album', 'num'),)", 'object_name': 'CD'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cds'", 'to': "orm['nonclassical.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        },
        'nonclassical.track': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('cd', 'num'),)", 'object_name': 'Track'},
            'cd': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': "orm['nonclassical.CD']"}),
            'dir_name': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'track'", 'unique': 'True', 'to': "orm['common.MusicFile']"}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['nonclassical']