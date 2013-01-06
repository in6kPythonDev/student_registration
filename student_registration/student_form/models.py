from django.db import models

class AboutInfo(models.Model):
    name = models.CharField(max_length = 100)
    test_migration = models.BooleanField()
    test_migration_two = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    e_mail = models.EmailField()
    phone = models.IntegerField(max_length = 10)
    password = models.CharField(max_length = 25)
    find_about_us = models.ForeignKey(AboutInfo)

    def __unicode__(self):
        return self.first_name