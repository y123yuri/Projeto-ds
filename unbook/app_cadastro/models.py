from django.db import models

# Create your models here.

class Cadastro(models.Model):
<<<<<<< HEAD
    nome_usuario = models.CharField(max_length=150, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=22, null=False, blank=False, unique=True, primary_key=True)
=======
    nome_usuario = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
>>>>>>> 098859d47ef34f5d02a0d1fbb6c0a66ccd05f8c4
    senha = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.email}: {self.nome_usuario}'