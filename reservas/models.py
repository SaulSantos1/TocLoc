from django.contrib.auth.models import AbstractUser
from django.db import models
from usuarios.models import Usuario
from django.utils.timezone import now
from datetime import time
from local.models import LocalEsportivo

class Reserva(models.Model):
    local = models.ForeignKey(LocalEsportivo, on_delete=models.CASCADE, related_name='reservas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_reservas')
    data = models.DateField(default=now)
    horario_inicio = models.TimeField(default=time(9, 0)) 
    horario_fim = models.TimeField(default=time(10, 0))

    class Meta:
        unique_together = ('local', 'data', 'horario_inicio', 'horario_fim')

    def __str__(self):
        return f"Reserva: {self.local.nome} por {self.usuario.username} em {self.data} ({self.horario_inicio} - {self.horario_fim})"
