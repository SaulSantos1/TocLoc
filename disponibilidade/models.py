from django.db import models
from local.models import LocalEsportivo
from django.utils.timezone import now
from datetime import time

class Disponibilidade(models.Model):
    local = models.ForeignKey(LocalEsportivo, on_delete=models.CASCADE, related_name='disponibilidades')
    data = models.DateField(default=now)  # Substituindo dia da semana pela data
    horario_inicio = models.TimeField(default=time(8, 0))  # Horário padrão: 08:00
    horario_fim = models.TimeField(default=time(18, 0))  

    class Meta:
        unique_together = ('local', 'data', 'horario_inicio', 'horario_fim')

    def __str__(self):
        return f"{self.local.nome} - {self.data} ({self.horario_inicio} - {self.horario_fim})"