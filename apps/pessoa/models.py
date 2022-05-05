from django.db import models

class Pessoa(models.Model):
    CPF = models.CharField(primary_key= True, max_length=14)
    nome = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Usuario(Pessoa):
    senha = models.CharField(max_length=30)
    funcao = models.CharField(max_length=1)

class Paciente(Pessoa):
    observacao = models.CharField(max_length=255)