from rest_framework import serializers, viewsets
 
from .models import Horario
 
 
class HorarioSerializer(serializers.ModelSerializer):
   class Meta:
       model = Horario
       fields = ('id_horario', 'prescricao_associada', 'status_correspondente', 'horario')
 
   # @permission_classes([IsAuthenticated])
class HorarioViewSet(viewsets.ModelViewSet):
   queryset = Horario.objects.all()
   serializer_class = HorarioSerializer