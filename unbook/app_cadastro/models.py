from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome_usuario = models.CharField(max_length=150, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=22, null=False, blank=False, unique=True, primary_key=True)
    senha = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.email}: {self.nome_usuario}'