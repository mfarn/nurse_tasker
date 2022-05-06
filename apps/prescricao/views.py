from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
 
from .models import Prescricao
 
 
class PrescricaoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Prescricao
       fields = ('id_prescricao', 'nome_droga', 'patologia', 'dosagem', 'cpf_paciente', 'cpf_cadastrante')
 
   # @permission_classes([IsAuthenticated])
class PrescricaoViewSet(viewsets.ModelViewSet):
   queryset = Prescricao.objects.all()
   serializer_class = PrescricaoSerializer

class PrescricaoView(APIView):
   def get(self, request, id_prescricao=None):
      if id_prescricao is None:
         cpf_cadastrante = request.GET.get('cpf_cadastrante')
         if cpf_cadastrante:
            qs = Prescricao.objects.filter(cpf_cadastrante = cpf_cadastrante)
         else:
            qs = Prescricao.objects.all()
         data = PrescricaoSerializer(qs, many = True).data
         return Response(data)
      qs = Prescricao.objects.filter(id_prescricao = id_prescricao)
      obj = get_object_or_404(Prescricao, id_prescricao = id_prescricao)
      data = PrescricaoSerializer(obj).data
      return Response(data)

   def post(self, request):
      serializer = PrescricaoSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         serializer.save()
         return Response(serializer.data)
      return Response({"invalid" : "Not good data"})

   def patch(self, request, id_prescricao=None):
      if id_prescricao is None:
         return Response({"invalid" : "No primary_keys offered"})
      obj = get_object_or_404(Prescricao, id_prescricao = id_prescricao)
      serializer = PrescricaoSerializer(obj, data=request.data, partial=True) # set partial=True to update a data partially
      if serializer.is_valid():
         serializer.save()
         return Response(code=201, data=serializer.data)
      return Response(code=400, data="wrong parameters")
    
prescricao_alt_view = PrescricaoView.as_view()