from rest_framework import serializers
from prescricao import models

class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescricao
        fields = '__all__'