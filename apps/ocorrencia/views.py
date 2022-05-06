from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from .models import Ocorrencia
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ('id_ocorrencia', 'tipo', 'descricao', 'cpf_paciente', 'usuario_cadastrante', 'prescicao_associada')

class OcorrenciaView(APIView):
    def get(self, request, id_ocorrencia=None):
        if id_ocorrencia is None:
            qs = Ocorrencia.objects.all()
            data = OcorrenciaSerializer(qs, many = True).data
            return Response(data)
        qs = Ocorrencia.objects.filter(id_ocorrencia = id_ocorrencia)
        obj = get_object_or_404(Ocorrencia, id_ocorrencia = id_ocorrencia)
        data = OcorrenciaSerializer(obj).data
        return Response(data)
    def post(self, request):
        serializer = OcorrenciaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid" : "Not good data"})
    

ocorrencia_alt_view = OcorrenciaView.as_view()
