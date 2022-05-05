from rest_framework import serializers, viewsets
 
from .models import Prescricao
 
 
class PrescricaoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Prescricao
       fields = ('id_prescricao', 'nome_droga', 'patologia', 'dosagem', 'cpf_paciente', ' cpf_cadastrante')
 
   # @permission_classes([IsAuthenticated])
class PrescricaoViewSet(viewsets.ModelViewSet):
   queryset = Prescricao.objects.all()
   serializer_class = PrescricaoSerializer