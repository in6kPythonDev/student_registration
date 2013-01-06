# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AboutInfo'
        db.create_table('student_form_aboutinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('student_form', ['AboutInfo'])

        # Adding model 'Student'
        db.create_table('student_form_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('e_mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('find_about_us', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student_form.AboutInfo'])),
        ))
        db.send_create_signal('student_form', ['Student'])


    def backwards(self, orm):
        # Deleting model 'AboutInfo'
        db.delete_table('student_form_aboutinfo')

        # Deleting model 'Student'
        db.delete_table('student_form_student')


    models = {
        'student_form.aboutinfo': {
            'Meta': {'object_name': 'AboutInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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