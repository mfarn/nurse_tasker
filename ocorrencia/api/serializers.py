from rest_framework import serializers
from ocorrencia import models

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ocorrencia
        fields = '__all__'