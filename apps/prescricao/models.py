from django.db import models
from uuid import  uuid4
 
from ..pessoa.models import Paciente,Usuario
 
class Prescricao(models.Model):
    id_prescricao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_droga = models.CharField(max_length=255)
    patologia = models.CharField(max_length=255)
    dosagem = models.CharField(max_length=255)
    status_atual = models.CharField(max_length=1)
    cpf_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    cpf_cadastrante = models.ForeignKey(Usuario, on_delete=models.CASCADE)