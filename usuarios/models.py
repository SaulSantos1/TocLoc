from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    USUARIO = 'usuario'
    ANFITRIAO = 'anfitriao'

    TIPO_USUARIO_CHOICES = [
        (USUARIO, 'Usuário'),
        (ANFITRIAO, 'Anfitrião'),
    ]
    TIPOS = (
        ('usuario', 'Usuário'),
        ('anfitriao', 'Anfitrião'),
    )
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS, default='usuario')
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)


    def is_usuario(self):
        return self.tipo_usuario == self.USUARIO

    def is_anfitriao(self):
        return self.tipo_usuario == self.ANFITRIAO