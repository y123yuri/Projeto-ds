from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
from datetime import timedelta
from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import AbstractUser




class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    total_denuncias = models.IntegerField(default=0)
    curso = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    semestre = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return  self.user.username


class Cadastro(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True, default=0)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=22, null=False, blank=False, unique=True, primary_key=True)
    password = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.email}: {self.username}'

# models.py


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # Opcional: defina uma validade para o token, por exemplo, 24 horas
        expiration_time = timedelta(hours=1)
        return self.created_at >= timezone.now() - expiration_time



class Cursos_unb(models.Model):
    curso = models.CharField(max_length=100, primary_key=True)
    pessoas = models.IntegerField(default=0)
    
    def __str__(self):
        return self.curso
    