from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=20)
    anio = models.IntegerField(default=2000)
    fechaDeAdquisicion = models.DateField()

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre


