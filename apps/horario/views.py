from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
 
from ..pessoa.views import UsuarioSerializer
from .models import Horario
 
 
class HorarioSerializer(serializers.ModelSerializer):
   usuario = UsuarioSerializer(many=False, read_only=True)

   class Meta:
       model = Horario
       fields = ('id_horario', 'prescricao_associada', 'status_correspondente', 'horario', 'cpf_responsavel', 'usuario')
 
   # @permission_classes([IsAuthenticated])
class HorarioViewSet(viewsets.ModelViewSet):
   queryset = Horario.objects.all()
   serializer_class = HorarioSerializer

class HorarioView(APIView):
   def get(self, request, prescricao_associada):
      if prescricao_associada is None:
         return Response({"invalid" : "No primary_keys offered"})
      qs = Horario.objects.filter(prescricao_associada=prescricao_associada)
      data = HorarioSerializer(qs, many = True).data
      return Response(data)
   def post(self, request):
      serializer = HorarioSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         serializer.save()
         return Response(serializer.data)
      return Response({"invalid" : "Not good data"})

horario_alt_view = HorarioView.as_view()