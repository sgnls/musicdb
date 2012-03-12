# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table('classical_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.IntegerField')(max_length=100, db_index=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('forenames', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('original_surname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('original_forenames', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('born', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('died', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('born_question', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('died_question', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='classical_artists', null=True, to=orm['common.Nationality'])),
            ('dir_name', self.gf('django.db.models.fields.IntegerField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('classical', ['Artist'])

        # Adding model 'Ensemble'
        db.create_table('classical_ensemble', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nationality', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ensembles', null=True, to=orm['common.Nationality'])),
            ('slug', self.gf('django.db.models.fields.IntegerField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('classical', ['Ensemble'])

        # Adding model 'Work'
        db.create_table('classical_work', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('composer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='works', to=orm['classical.Artist'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year_question', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('key', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='works', null=True, to=orm['classical.Key'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='works', null=True, to=orm['classical.Category'])),
            ('slug', self.gf('django.db.models.fields.IntegerField')(max_length=100, db_index=True)),
            ('sort_value', self.gf('django.db.models.fields.IntegerField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('classical', ['Work'])

        # Adding model 'WorkRelationship'
        db.create_table('classical_workrelationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source_relations', to=orm['classical.Work'])),
            ('derived', self.gf('django.db.models.fields.related.ForeignKey')(related_name='derived_relations', to=orm['classical.Work'])),
            ('nature', self.gf('django.db.models.fields.CharField')(max_length=13)),
        ))
        db.send_create_signal('classical', ['WorkRelationship'])

        # Adding model 'Catalogue'
        db.create_table('classical_catalogue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catalogues', to=orm['classical.Artist'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('classical', ['Catalogue'])

        # Adding unique constraint on 'Catalogue', fields ['artist', 'num']
        db.create_unique('classical_catalogue', ['artist_id', 'num'])

        # Adding unique constraint on 'Catalogue', fields ['artist', 'prefix']
        db.create_unique('classical_catalogue', ['artist_id', 'prefix'])

        # Adding model 'WorkCatalogue'
        db.create_table('classical_workcatalogue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catalogues', to=orm['classical.Work'])),
            ('catalogue', self.gf('django.db.models.fields.related.ForeignKey')(related_name='works', to=orm['classical.Catalogue'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('classical', ['WorkCatalogue'])

        # Adding model 'Category'
        db.create_table('classical_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('numchild', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('long_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.IntegerField')(max_length=100, db_index=True)),
        ))
        db.send_create_signal('classical', ['Category'])

        # Adding model 'Instrument'
        db.create_table('classical_instrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('noun', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('adjective', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('classical', ['Instrument'])

        # Adding model 'Key'
        db.create_table('classical_key', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('minor', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('classical', ['Key'])

        # Adding unique constraint on 'Key', fields ['name', 'minor']
        db.create_unique('classical_key', ['name', 'minor'])

        # Adding model 'Recording'
        db.create_table('classical_recording', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recordings', to=orm['classical.Work'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.IntegerField')(max_length=100, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow, null=True)),
        ))
        db.send_create_signal('classical', ['Recording'])

        # Adding model 'Movement'
        db.create_table('classical_movement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recording', self.gf('django.db.models.fields.related.ForeignKey')(related_name='movements', to=orm['classical.Recording'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('music_file', self.gf('django.db.models.fields.related.OneToOneField')(related_name='movement', unique=True, to=orm['common.MusicFile'])),
            ('section_title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('classical', ['Movement'])

        # Adding unique constraint on 'Movement', fields ['recording', 'num']
        db.create_unique('classical_movement', ['recording_id', 'num'])

        # Adding model 'Performance'
        db.create_table('classical_performance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recording', self.gf('django.db.models.fields.related.ForeignKey')(related_name='performances', to=orm['classical.Recording'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('subclass', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('classical', ['Performance'])

        # Adding unique constraint on 'Performance', fields ['recording', 'num']
        db.create_unique('classical_performance', ['recording_id', 'num'])

        # Adding model 'ArtistPerformance'
        db.create_table('classical_artistperformance', (
            ('performance_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['classical.Performance'], unique=True, primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='performances', to=orm['classical.Artist'])),
            ('instrument', self.gf('django.db.models.fields.related.ForeignKey')(related_name='performances', to=orm['classical.Instrument'])),
        ))
        db.send_create_signal('classical', ['ArtistPerformance'])

        # Adding model 'EnsemblePerformance'
        db.create_table('classical_ensembleperformance', (
            ('performance_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['classical.Performance'], unique=True, primary_key=True)),
            ('ensemble', self.gf('django.db.models.fields.related.ForeignKey')(related_name='performances', to=orm['classical.Ensemble'])),
        ))
        db.send_create_signal('classical', ['EnsemblePerformance'])

    def backwards(self, orm):
        # Removing unique constraint on 'Performance', fields ['recording', 'num']
        db.delete_unique('classical_performance', ['recording_id', 'num'])

        # Removing unique constraint on 'Movement', fields ['recording', 'num']
        db.delete_unique('classical_movement', ['recording_id', 'num'])

        # Removing unique constraint on 'Key', fields ['name', 'minor']
        db.delete_unique('classical_key', ['name', 'minor'])

        # Removing unique constraint on 'Catalogue', fields ['artist', 'prefix']
        db.delete_unique('classical_catalogue', ['artist_id', 'prefix'])

        # Removing unique constraint on 'Catalogue', fields ['artist', 'num']
        db.delete_unique('classical_catalogue', ['artist_id', 'num'])

        # Deleting model 'Artist'
        db.delete_table('classical_artist')

        # Deleting model 'Ensemble'
        db.delete_table('classical_ensemble')

        # Deleting model 'Work'
        db.delete_table('classical_work')

        # Deleting model 'WorkRelationship'
        db.delete_table('classical_workrelationship')

        # Deleting model 'Catalogue'
        db.delete_table('classical_catalogue')

        # Deleting model 'WorkCatalogue'
        db.delete_table('classical_workcatalogue')

        # Deleting model 'Category'
        db.delete_table('classical_category')

        # Deleting model 'Instrument'
        db.delete_table('classical_instrument')

        # Deleting model 'Key'
        db.delete_table('classical_key')

        # Deleting model 'Recording'
        db.delete_table('classical_recording')

        # Deleting model 'Movement'
        db.delete_table('classical_movement')

        # Deleting model 'Performance'
        db.delete_table('classical_performance')

        # Deleting model 'ArtistPerformance'
        db.delete_table('classical_artistperformance')

        # Deleting model 'EnsemblePerformance'
        db.delete_table('classical_ensembleperformance')

    models = {
        'classical.artist': {
            'Meta': {'ordering': "('surname', 'forenames', 'born')", 'object_name': 'Artist'},
            'born': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'born_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'died': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'died_question': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dir_name': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'db_index': 'True'}),
            'forenames': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'classical_artists'", 'null': 'True', 'to': "orm['common.Nationality']"}),
            'original_forenames': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'original_surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'db_index': 'True'}),
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
        'classical.category': {
            'Meta': {'ordering': "('path',)", 'object_name': 'Category'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'classical.ensemble': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Ensemble'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nationality': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ensembles'", 'null': 'True', 'to': "orm['common.Nationality']"}),
            'slug': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'db_index': 'True'})
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'db_index': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recordings'", 'to': "orm['classical.Work']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'classical.work': {
            'Meta': {'ordering': "('sort_value',)", 'object_name': 'Work'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'works'", 'null': 'True', 'to': "orm['classical.Category']"}),
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'works'", 'to': "orm['classical.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'works'", 'null': 'True', 'to': "orm['classical.Key']"}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'db_index': 'True'}),
            'sort_value': ('django.db.models.fields.IntegerField', [], {'max_length': '100', 'db_index': 'True'}),
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
        }
    }

    complete_apps = ['classical']