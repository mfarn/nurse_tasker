from rest_framework import serializers
from pessoa import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'
