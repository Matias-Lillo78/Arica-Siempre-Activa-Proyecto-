from django.db import models

class Actividad(models.Model):
    titulo = models.CharField('Nombre de la actividad', max_length=150)
    categoria = models.CharField('Categoría', max_length=50, blank=True)
    fecha = models.DateField('Fecha')
    descripcion = models.TextField('Descripción', blank=True)
    precio = models.IntegerField('Precio', default=0)
    cupo_maximo = models.IntegerField('Cupo máximo', null=True, blank=True)
    imagen = models.ImageField(upload_to='static/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo