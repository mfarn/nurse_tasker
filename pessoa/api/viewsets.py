from rest_framework import viewsets
from pessoa.api import serializers
from pessoa import models


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PacienteSerializer
    queryset = models.Paciente.objects.all()