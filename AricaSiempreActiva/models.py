from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField('Nombre del evento', max_length=150)
    lugar = models.CharField('Lugar', max_length=150)
    fecha = models.DateField('Fecha del evento')
    descripcion = models.TextField('Descripción', blank=True)

    def __str__(self):
        return self.titulo

class Suscriptor(models.Model):
    correo = models.EmailField('Correo', unique=True)
    fecha = models.DateTimeField('Fecha de suscripción', auto_now_add=True)

    def __str__(self):
        return self.correo