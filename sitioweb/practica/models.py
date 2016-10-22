from django.db import models


class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=50)
    carnet = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='carnet')
    ciclo = models.IntegerField()

    

    class Meta:
        managed = False
        db_table = 'asignacion'



class Estudiante(models.Model):
    carnet = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    

    class Meta:
        managed = False
        db_table = 'estudiante'
    
