# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Round'
        db.create_table('roulette_round', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('minimum_players', self.gf('django.db.models.fields.IntegerField')(default=25)),
            ('round_end', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 9, 2, 19, 55, 17, 356716), blank=True)),
        ))
        db.send_create_signal('roulette', ['Round'])

        # Adding model 'Bullet'
        db.create_table('roulette_bullet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tweet', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('roulette_round', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roulette.Round'])),
            ('date_submitted', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 9, 1, 19, 55, 17, 357828), blank=True)),
        ))
        db.send_create_signal('roulette', ['Bullet'])

        # Adding model 'Vote'
        db.create_table('roulette_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('bullet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roulette.Bullet'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('roulette', ['Vote'])


    def backwards(self, orm):
        
        # Deleting model 'Round'
        db.delete_table('roulette_round')

        # Deleting model 'Bullet'
        db.delete_table('roulette_bullet')

        # Deleting model 'Vote'
        db.delete_table('roulette_vote')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'roulette.bullet': {
            'Meta': {'object_name': 'Bullet'},
            'date_submitted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 9, 1, 19, 55, 17, 357828)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roulette_round': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roulette.Round']"}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'roulette.round': {
            'Meta': {'object_name': 'Round'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_players': ('django.db.models.fields.IntegerField', [], {'default': '25'}),
            'round_end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 9, 2, 19, 55, 17, 356716)', 'blank': 'True'})
        },
        'roulette.vote': {
            'Meta': {'object_name': 'Vote'},
            'bullet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roulette.Bullet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['roulette']
