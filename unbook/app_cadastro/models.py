from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome_usuario = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=22, null=False, blank=False)
    senha = models.CharField(max_length=30, null=False, blank=False)
