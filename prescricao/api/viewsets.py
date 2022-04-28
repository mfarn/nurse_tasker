from rest_framework import viewsets
from prescricao.api import serializers
from prescricao import models


class PrescricaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PrescricaoSerializer
    queryset = models.Prescricao.objects.all()