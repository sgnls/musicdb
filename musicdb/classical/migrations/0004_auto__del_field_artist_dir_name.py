# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Artist.dir_name'
        db.delete_column('classical_artist', 'dir_name')

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Artist.dir_name'
        raise RuntimeError("Cannot reverse this migration. 'Artist.dir_name' and its values cannot be restored.")
    models = {
        'classical.artist': {
            'Meta': {'ordering': "('surname', 'forenames', 'born')", 'object_name': 'Artist'},
            'born': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'born_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'died': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'died_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'forenames': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'classical_artists'", 'null': 'True', 'to': "orm['common.Nationality']"}),
            'original_forenames': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'original_surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'classical.artistperformance': {
            'Meta': {'ordering': "('instrument',)", 'object_name': 'ArtistPerformance', '_ormbases': ['classical.Performance']},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': "orm['classical.Artist']"}),
            'instrument': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': "orm['classical.Instrument']"}),
            'performance_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['classical.Performance']", 'unique': 'True', 'primary_key': 'True'})
        },
        'classical.catalogue': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('artist', 'num'), ('artist', 'prefix'))", 'object_name': 'Catalogue'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogues'", 'to': "orm['classical.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'classical.ensemble': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ensemble'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ensembles'", 'null': 'True', 'to': "orm['common.Nationality']"}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'classical.ensembleperformance': {
            'Meta': {'ordering': "('num',)", 'object_name': 'EnsemblePerformance', '_ormbases': ['classical.Performance']},
            'ensemble': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': "orm['classical.Ensemble']"}),
            'performance_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['classical.Performance']", 'unique': 'True', 'primary_key': 'True'})
        },
        'classical.instrument': {
            'Meta': {'ordering': "('noun',)", 'object_name': 'Instrument'},
            'adjective': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noun': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'classical.key': {
            'Meta': {'ordering': "('name', 'minor')", 'unique_together': "(('name', 'minor'),)", 'object_name': 'Key'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '13'})
        },
        'classical.movement': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('recording', 'num'),)", 'object_name': 'Movement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_file': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'movement'", 'unique': 'True', 'to': "orm['common.MusicFile']"}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'recording': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movements'", 'to': "orm['classical.Recording']"}),
            'section_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'classical.performance': {
            'Meta': {'ordering': "('num',)", 'unique_together': "(('recording', 'num'),)", 'object_name': 'Performance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'recording': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'performances'", 'to': "orm['classical.Recording']"}),
            'subclass': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'classical.recording': {
            'Meta': {'object_name': 'Recording'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recordings'", 'to': "orm['classical.Work']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'classical.work': {
            'Meta': {'ordering': "('sort_value',)", 'object_name': 'Work'},
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'works'", 'to': "orm['classical.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'works'", 'null': 'True', 'to': "orm['classical.Key']"}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'sort_value': ('django.db.models.fields.TextField', [], {'max_length': '100', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'classical.workcatalogue': {
            'Meta': {'ordering': "('catalogue__num',)", 'object_name': 'WorkCatalogue'},
            'catalogue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'works'", 'to': "orm['classical.Catalogue']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogues'", 'to': "orm['classical.Work']"})
        },
        'classical.workrelationship': {
            'Meta': {'object_name': 'WorkRelationship'},
            'derived': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'derived_relations'", 'to': "orm['classical.Work']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nature': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_relations'", 'to': "orm['classical.Work']"})
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

    complete_apps = ['classical']