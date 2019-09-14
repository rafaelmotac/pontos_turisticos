from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['get'], detail=False)
    def aprovados(self, request):
        pontos_aprovados = PontoTuristico.objects.filter(aprovado=True)
        serializer = self.get_serializer(pontos_aprovados, many=True)
        return Response(serializer.data)

