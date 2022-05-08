from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Usuario, Paciente

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('CPF', 'nome', 'senha', 'funcao')
        extra_kwargs = {'senha': {'write_only': True, 'min_length': 8}}

class PacienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paciente
        fields = ('CPF', 'nome', 'observacao')


# Usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioView(APIView):
    def get(self, request, CPF=None):
        if CPF is None:
            qs = Usuario.objects.all()
            data = UsuarioSerializer(qs, many = True).data
            return Response(data)
        qs = Usuario.objects.filter(CPF=CPF)
        obj = get_object_or_404(Usuario, CPF=CPF)
        data = UsuarioSerializer(obj).data
        return Response(data)

usuario_alt_view = UsuarioView.as_view()


# Paciente
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteView(APIView):
    def get(self, request, CPF=None):
        if CPF is None:
            qs = Paciente.objects.all()
            data = PacienteSerializer(qs, many = True).data
            return Response(data)
        qs = Paciente.objects.filter(CPF=CPF)
        obj = get_object_or_404(Paciente, CPF=CPF)
        data = PacienteSerializer(obj).data
        return Response(data)

paciente_alt_view = PacienteView.as_view()