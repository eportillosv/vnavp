from distutils.command import upload
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    image = models.ImageField(upload_to='imagenes/', null = True, verbose_name='Imagen')
    description = models.TextField(null=True, verbose_name='Descripción')

    def __str__(self):
        fila = "Nombre: " + self.name + " - " +"Descripción: " + self.description
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()