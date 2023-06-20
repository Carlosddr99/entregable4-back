from django.db import models

# Create your models here.


class Asignatura (models.Model):

    nombre = models.CharField(max_length=20, null=False)
    curso = models.IntegerField(null=False, default=3)

