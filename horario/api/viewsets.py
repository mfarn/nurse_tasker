from rest_framework import viewsets
from horario.api import serializers
from horario import models

class HorarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HorarioSerializer
    queryset = models.Horario.objects.all()