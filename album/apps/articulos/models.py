from django import forms
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=55)
    fecha_publicacion = models.DateField() 
    resumen = models.TextField(max_length=200)
    detalle = models.TextField()
    imagen_cover = models.ImageField(upload_to='noticias/covers/', null=True, blank=True)
    imagen_estatica = models.ImageField(upload_to='noticias/estaticas/', null=True, blank=True)
    imagen_dinamica = models.ImageField(upload_to='noticias/dinamicas/', null=True, blank=True)
    publicada = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


