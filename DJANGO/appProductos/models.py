from django.db import models

# Create your models here.
class productos(models.Model):
    codigoProductos = models.IntegerField()
    descripcionProductos = models.CharField(max_length=255)
    estatus = models.BooleanField()