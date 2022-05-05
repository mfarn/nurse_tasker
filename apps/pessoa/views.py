from rest_framework import serializers, viewsets

from .models import Usuario, Paciente

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('CPF', 'nome', 'senha', 'funcao')
        extra_kwargs = {'senha': {'write_only': True, 'min_length': 8}}

    # @permission_classes([IsAuthenticated])
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('CPF', 'nome', 'observacao')

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
