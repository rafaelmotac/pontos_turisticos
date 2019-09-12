from rest_framework import serializers

from core.models import PontoTuristico


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = serializers.StringRelatedField(many=True)
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'atracoes']
