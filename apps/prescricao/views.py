from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from ..horario.views import HorarioSerializer
 
from .models import Prescricao
from ..pessoa.models import Usuario

def get_min_cpf_filter(func):
   usuarios = Usuario.objects.filter(funcao = func)
   
   min_cpf = "-1"
   min_cpf_count = 1000000

   for usuario in usuarios:
      cpf_count = Prescricao.objects.filter(responsavel_atual = usuario.CPF).count()
      if cpf_count < min_cpf_count:
         min_cpf = usuario.CPF
         min_cpf_count = cpf_count

   return min_cpf

def next_status(status):
   if status == 'P':
      return 'D'
   if status == 'D':
      return 'R'
   if status == 'R':
      return 'A'
   else:
      return status
 
class PrescricaoSerializer(serializers.ModelSerializer):
   tasks = HorarioSerializer(many=True, read_only=True)

   class Meta:
       model = Prescricao
       fields = ('id_prescricao', 'nome_droga', 'dosagem', 'cpf_paciente', 'horario_previsto', 'status_atual',
                 'cpf_cadastrante', 'responsavel_atual', 'tasks')
 
   # @permission_classes([IsAuthenticated])
class PrescricaoViewSet(viewsets.ModelViewSet):
   queryset = Prescricao.objects.all()
   serializer_class = PrescricaoSerializer

class PrescricaoView(APIView):
   
   def get(self, request, usuario=None, id_prescricao=None):

      if id_prescricao:
         obj = get_object_or_404(Prescricao, id_prescricao = id_prescricao)
         data = PrescricaoSerializer(obj).data
         return Response(data)

      if usuario == None:
         qs = Prescricao.objects.all()
         data = PrescricaoSerializer(qs, many=True).data
         return Response(data)


      usuario_func = Usuario.objects.filter(CPF = usuario).first().funcao
      if usuario_func == 'M':
         qs = Prescricao.objects.filter(cpf_cadastrante = usuario)
         data = PrescricaoSerializer(qs, many=True).data
         return Response(data)
      
      else:
         qs = Prescricao.objects.filter(responsavel_atual = usuario)
         data = PrescricaoSerializer(qs, many=True).data
         return Response(data)

   def post(self, request):
      data = request.data
      data['responsavel_atual'] = get_min_cpf_filter('F')
      data['status_atual'] = 'P'
      
      serializer = PrescricaoSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         serializer.save()

         data_horario = {'prescricao_associada':serializer.data['id_prescricao'],
                        'status_correspondente':'P',
                         'cpf_responsavel':data['cpf_cadastrante']}
         serializer_horario = HorarioSerializer(data=data_horario)

         if serializer_horario.is_valid(raise_exception=True):
            serializer_horario.save()
         
         return Response(serializer.data)
      return Response({"invalid" : "Not good data"})

   def patch(self, request, id_prescricao=None):

      if request.data:
         obj = get_object_or_404(Prescricao, id_prescricao = id_prescricao)
         serializer = PrescricaoSerializer(obj, data=request.data, partial=True) # set partial=True to update a data partially
         if serializer.is_valid(raise_exception=True):
            serializer.save()
         return Response(status=201, data=serializer.data)

      obj = get_object_or_404(Prescricao, id_prescricao = id_prescricao)

      data = {}
      data['status_atual'] = next_status(obj.status_atual)

      if data['status_atual'] == 'A':
         data['responsavel_atual'] = obj.cpf_cadastrante.CPF

      else:
         data['responsavel_atual'] = get_min_cpf_filter('E')
       
      serializer = PrescricaoSerializer(obj, data=data, partial=True) # set partial=True to update a data partially
      if serializer.is_valid():

         data_horario = {'prescricao_associada':obj.id_prescricao,
                        'status_correspondente':next_status(obj.status_atual),
                         'cpf_responsavel':obj.responsavel_atual.CPF}
         serializer_horario = HorarioSerializer(data=data_horario)

         if serializer_horario.is_valid(raise_exception=True):
            serializer_horario.save()

         serializer.save()
         return Response(status=201, data=serializer.data)

      return Response(status=400, data="wrong parameters")
    
prescricao_alt_view = PrescricaoView.as_view()