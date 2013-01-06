# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AboutInfo.test_migration_two'
        db.add_column('student_form_aboutinfo', 'test_migration_two',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AboutInfo.test_migration_two'
        db.delete_column('student_form_aboutinfo', 'test_migration_two')


    models = {
        'student_form.aboutinfo': {
            'Meta': {'object_name': 'AboutInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'test_migration': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'test_migration_two': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        'student_form.student': {
            'Meta': {'object_name': 'Student'},
            'e_mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'find_about_us': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['student_form.AboutInfo']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['student_form']