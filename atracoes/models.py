from django.db import models

from core.models import PontoTuristico


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_fun = models.TextField()
    idade_minima = models.IntegerField()
    ponto_turistico = models.ForeignKey(PontoTuristico, related_name='atracoes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
