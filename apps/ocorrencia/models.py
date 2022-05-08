from django.db import models
from uuid import uuid4
from ..prescricao.models import Prescricao
from ..pessoa.models import Usuario

class Ocorrencia(models.Model):
    id_ocorrencia = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    prescricao_associada = models.ForeignKey(Prescricao, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=2)
    descricao = models.CharField(max_length=255)
    usuario_cadastrante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
