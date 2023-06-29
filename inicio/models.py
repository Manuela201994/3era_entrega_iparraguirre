from django.db import models

# Create your models here.

class Adoptantes(models.Model):
    nombre =  models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono =  models.IntegerField()
    mensaje = models.DateField(null=True)
    