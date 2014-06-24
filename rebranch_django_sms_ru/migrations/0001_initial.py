# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'sms_ru_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'content_type_set_for_message', null=True, to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('api_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sent', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('queue_type', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'rebranch_django_sms_ru', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'sms_ru_message')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rebranch_django_sms_ru.message': {
            'Meta': {'ordering': "[u'-created']", 'object_name': 'Message', 'db_table': "u'sms_ru_message'"},
            'api_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'content_type_set_for_message'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'queue_type': ('django.db.models.fields.IntegerField', [], {}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['rebranch_django_sms_ru']