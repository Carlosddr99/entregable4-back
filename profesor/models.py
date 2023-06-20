from django.db import models
from asignatura.models import Asignatura
# Create your models here.



class Profesor (models.Model):

    nombre = models.CharField(max_length=20, null=False)
    edad = models.IntegerField( null=False, default=3)
    asignatura = models.ForeignKey(Asignatura, blank=True, null=True, on_delete=models.CASCADE)
