from rest_framework import serializers

from atracoes.models import Atracao
from core.api.serializers import PontoTuristicoSerializer


class AtracaoSerializer(serializers.ModelSerializer):
    ponto_turistico = PontoTuristicoSerializer()
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao', 'horario_fun', 'idade_minima', 'ponto_turistico']
