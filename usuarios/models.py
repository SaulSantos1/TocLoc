from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    VISITANTE = 'visitante'
    USUARIO = 'usuario'
    ANFITRIAO = 'anfitriao'

    TIPO_USUARIO_CHOICES = [
        (VISITANTE, 'Visitante'),
        (USUARIO, 'Usuário'),
        (ANFITRIAO, 'Anfitrião'),
    ]
    TIPOS = (
        ('visitante', 'Visitante'),
        ('usuario', 'Usuário'),
        ('anfitriao', 'Anfitrião'),
    )
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS, default='visitante')
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def is_visitante(self):
        return self.tipo_usuario == self.VISITANTE

    def is_usuario(self):
        return self.tipo_usuario == self.USUARIO

    def is_anfitriao(self):
        return self.tipo_usuario == self.ANFITRIAO