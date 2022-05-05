from rest_framework import serializers, viewsets
from .models import Ocorrencia


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ('id_ocorrencia', 'tipo', 'descricao', 'cpf_paciente', 'usuario_cadastrante', 'prescicao_associada')

class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer