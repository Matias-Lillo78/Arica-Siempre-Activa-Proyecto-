
from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):

    ROLES = [
        ('turista', 'Turista'),
        ('gremio', 'Gremio'),
        ('moderador', 'Moderador'),
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='turista'
    )

    def __str__(self):
        return '{} - {}'.format(
            self.usuario.username,
            self.get_rol_display()
        )
