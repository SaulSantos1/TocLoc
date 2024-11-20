from django.db import models
from usuarios.models import Usuario

class LocalEsportivo(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    capacidade = models.IntegerField()
    anfitriao = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="locais", blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nome
