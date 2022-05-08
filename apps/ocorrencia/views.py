from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from .models import Ocorrencia
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..prescricao.models import Prescricao
from ..prescricao.views import PrescricaoSerializer

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ('id_ocorrencia', 'prescricao_associada', 'tipo', 'descricao', 'usuario_cadastrante')

class OcorrenciaView(APIView):

    def get(self, request, prescricao=None):

        if prescricao == None:
            qs = Ocorrencia.objects.all()
            data = OcorrenciaSerializer(qs, many=True).data
            return Response(data)

        qs = Ocorrencia.objects.filter(prescricao_associada = prescricao).first()
        data = OcorrenciaSerializer(qs).data

        return Response(data)

    def post(self, request):

        obj = Prescricao.objects.filter(id_prescricao = request.data['prescricao_associada']).first()
        
        data = {}
        data['status_atual'] = 'C'
        data['responsavel_atual'] = obj.cpf_cadastrante.CPF
        serializer = PrescricaoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

        serializer = OcorrenciaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid" : "Not good data"})
    
ocorrencia_alt_view = OcorrenciaView.as_view()
