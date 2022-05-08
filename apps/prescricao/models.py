from django.db import models
from uuid import  uuid4
 
from ..pessoa.models import Paciente, Usuario
 
class Prescricao(models.Model):
    id_prescricao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_droga = models.CharField(max_length=255)
    dosagem = models.CharField(max_length=255)
    horario_previsto = models.DateTimeField(auto_now=True)
    status_atual = models.CharField(max_length=1)
    cpf_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cpf_cadastrante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cadastrante')
    responsavel_atual = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='responsavel_atual')
    