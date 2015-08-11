# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artist.image_hash'
        db.add_column(u'classical_artist', 'image_hash',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8, blank=True),
                      keep_default=False)

        # Adding field 'Artist.image_exists'
        db.add_column(u'classical_artist', 'image_exists',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Artist.image_hash'
        db.delete_column(u'classical_artist', 'image_hash')

        # Deleting field 'Artist.image_exists'
        db.delete_column(u'classical_artist', 'image_exists')

    models = {
        u'classical.artist': {
            'Meta': {'ordering': "('surname', 'forenames', 'born')", 'object_name': 'Artist'},
            'born': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'born_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'died': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'died_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'forenames': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'classical_artists'", 'null': 'True', 'to': u"orm['common.Nationality']"}),
            'original_forenames': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'original_surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'classical.artistperformance': {
            'Meta': {'ordering': "('instrument',)", 'object_name': 'ArtistPerformance', '_ormbases': [u'classical.Performance']},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': u"orm['classical.Artist']"}),
            'instrument': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': u"orm['classical.Instrument']"}),
            u'performance_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['classical.Performance']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'classical.catalogue': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('artist', 'num'), ('artist', 'prefix'))", 'object_name': 'Catalogue'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogues'", 'to': u"orm['classical.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'classical.ensemble': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ensemble'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ensembles'", 'null': 'True', 'to': u"orm['common.Nationality']"}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'classical.ensembleperformance': {
            'Meta': {'ordering': "('num',)", 'object_name': 'EnsemblePerformance', '_ormbases': [u'classical.Performance']},
            'ensemble': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': u"orm['classical.Ensemble']"}),
            u'performance_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['classical.Performance']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'classical.instrument': {
            'Meta': {'ordering': "('noun',)", 'object_name': 'Instrument'},
            'adjective': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noun': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'classical.key': {
            'Meta': {'ordering': "('name', 'minor')", 'unique_together': "(('name', 'minor'),)", 'object_name': 'Key'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '13'})
        },
        u'classical.movement': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('recording', 'num'),)", 'object_name': 'Movement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'movement'", 'unique': 'True', 'to': u"orm['common.MusicFile']"}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'recording': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movements'", 'to': u"orm['classical.Recording']"}),
            'section_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'classical.performance': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('recording', 'num'),)", 'object_name': 'Performance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'recording': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': u"orm['classical.Recording']"}),
            'subclass': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'classical.recording': {
            'Meta': {'object_name': 'Recording'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recordings'", 'to': u"orm['classical.Work']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'classical.work': {
            'Meta': {'ordering': "('sort_value',)", 'object_name': 'Work'},
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'works'", 'to': u"orm['classical.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'works'", 'null': 'True', 'to': u"orm['classical.Key']"}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'sort_value': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'classical.workcatalogue': {
            'Meta': {'ordering': "('catalogue__num',)", 'object_name': 'WorkCatalogue'},
            'catalogue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'works'", 'to': u"orm['classical.Catalogue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogues'", 'to': u"orm['classical.Work']"})
        },
        u'classical.workrelationship': {
            'Meta': {'object_name': 'WorkRelationship'},
            'derived': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'derived_relations'", 'to': u"orm['classical.Work']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nature': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_relations'", 'to': u"orm['classical.Work']"})
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
        },
        u'common.nationality': {
            'Meta': {'ordering': "('noun',)", 'object_name': 'Nationality'},
            'adjective': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noun': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['classical']