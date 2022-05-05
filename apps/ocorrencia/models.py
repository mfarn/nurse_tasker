from django.db import models
from uuid import  uuid4
from ..prescricao.models import Prescricao
from ..pessoa.models import Paciente,Usuario

class Ocorrencia(models.Model):
    id_ocorrencia = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tipo = models.CharField(max_length=2)
    descricao = models.CharField(max_length=255)
    cpf_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    usuario_cadastrante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    prescicao_associada = models.ForeignKey(Prescricao , on_delete=models.CASCADE)