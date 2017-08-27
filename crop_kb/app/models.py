# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Crop(models.Model):
    crop_id = models.AutoField(primary_key=True)
    crop = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crop'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Farming(models.Model):
    fid = models.AutoField(primary_key=True)
    crop = models.ForeignKey(Crop, models.DO_NOTHING, blank=True, null=True)
    ftime = models.ForeignKey('Ftime', models.DO_NOTHING, blank=True, null=True)
    ftype = models.ForeignKey('Ftype', models.DO_NOTHING, blank=True, null=True)
    fdetail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farming'


class Ftime(models.Model):
    ftime_id = models.AutoField(primary_key=True)
    ftime = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ftime'


class Ftype(models.Model):
    ftype_id = models.AutoField(primary_key=True)
    ftype = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ftype'
