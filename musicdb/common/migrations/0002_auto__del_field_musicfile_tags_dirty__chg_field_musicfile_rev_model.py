# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'MusicFile.rev_model'
        db.alter_column(u'common_musicfile', 'rev_model', self.gf('django.db.models.fields.CharField')(max_length=24))

    def backwards(self, orm):

        # Changing field 'MusicFile.rev_model'
        db.alter_column(u'common_musicfile', 'rev_model', self.gf('django.db.models.fields.CharField')(max_length=8))
    models = {
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
        },
        u'common.nationality': {
            'Meta': {'ordering': "('noun',)", 'object_name': 'Nationality'},
            'adjective': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noun': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['common']
