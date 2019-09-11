from django.contrib.auth.models import User
from django.db import models

from core.models import PontoTuristico


class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    data = models.DateTimeField(auto_now_add=True)
    ponto_turistico = models.ForeignKey(PontoTuristico, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
