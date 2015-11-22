# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'audiobooks_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('first_names', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.TextField')(max_length=100, db_index=True)),
            ('last_name_first', self.gf('django.db.models.fields.TextField')(max_length=1, db_index=True)),
        ))
        db.send_create_signal(u'audiobooks', ['Author'])

        # Adding model 'AudioBook'
        db.create_table(u'audiobooks_audiobook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='books', to=orm['audiobooks.Author'])),
            ('image_hash', self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True)),
            ('image_exists', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'audiobooks', ['AudioBook'])

        # Adding model 'Track'
        db.create_table(u'audiobooks_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audiobook', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tracks', to=orm['audiobooks.AudioBook'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('music_file', self.gf('django.db.models.fields.related.OneToOneField')(related_name='audiobook_track', unique=True, to=orm['common.MusicFile'])),
        ))
        db.send_create_signal(u'audiobooks', ['Track'])

        # Adding unique constraint on 'Track', fields ['audiobook', 'num']
        db.create_unique(u'audiobooks_track', ['audiobook_id', 'num'])

    def backwards(self, orm):
        # Removing unique constraint on 'Track', fields ['audiobook', 'num']
        db.delete_unique(u'audiobooks_track', ['audiobook_id', 'num'])

        # Deleting model 'Author'
        db.delete_table(u'audiobooks_author')

        # Deleting model 'AudioBook'
        db.delete_table(u'audiobooks_audiobook')

        # Deleting model 'Track'
        db.delete_table(u'audiobooks_track')

    models = {
        u'audiobooks.audiobook': {
            'Meta': {'ordering': "('title',)", 'object_name': 'AudioBook'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': u"orm['audiobooks.Author']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'audiobooks.author': {
            'Meta': {'ordering': "('last_name', 'first_names')", 'object_name': 'Author'},
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
            'rev_model': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['audiobooks']