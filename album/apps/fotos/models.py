from django.db import models

# Create your models here.

class Mifoto(models.Model):
    nombre = models.CharField(max_length=90)
    descripcion = models.CharField( max_length=2000 )
    imageurl = models.URLField(max_length=500, null=True, blank=True)  # Cambiado a URLField
    publish = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre