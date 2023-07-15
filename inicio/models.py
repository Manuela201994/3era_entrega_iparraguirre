from django.db import models

# Create your models here.

class Adoptantes(models.Model):
    nombre =  models.CharField(max_length=20)
    edad = models.CharField(max_length=3)
    telefono = models.CharField(max_length=20)
    mensaje = models.CharField(max_length=100)
    