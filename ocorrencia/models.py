from pyexpat import model
from django.db import models
from uuid import  uuid4

class Ocorrencia(models.Model):
    id_ocorrencia = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tipo = models.CharField(max_length=2)
    descricao = models.CharField(max_length=255)
    cpf_paciente = models.ForeignKey('pessoa.Paciente', on_delete=models.CASCADE)
    usuario_cadastrante = models.ForeignKey('pessoa.Usuario', on_delete=models.CASCADE)
    prescicao_associada = models.ForeignKey('prescricao.Prescricao', on_delete=models.CASCADE)