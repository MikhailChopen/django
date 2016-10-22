# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=50)
    carnet = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='carnet')
    ciclo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asignacion'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Estudiante(models.Model):
    carnet = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estudiante'
