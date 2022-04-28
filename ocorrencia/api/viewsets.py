from rest_framework import viewsets
from ocorrencia.api import serializers
from ocorrencia import models

class OcorrenciaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OcorrenciaSerializer
    queryset = models.Ocorrencia.objects.all()