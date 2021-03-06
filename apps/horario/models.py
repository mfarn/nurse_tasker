from django.db import models
from uuid import  uuid4

from ..prescricao.models import Prescricao

class Horario(models.Model):
    id_horario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    prescricao_associada = models.ForeignKey(Prescricao, on_delete=models.CASCADE)
    status_correspondente = models.CharField(max_length=1)
    horario = models.DateTimeField(auto_now=True)