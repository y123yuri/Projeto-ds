from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime
from datetime import timedelta
from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import AbstractUser







class Cadastro(models.Model):
    username = models.CharField(max_length=150, null=False, blank=False, unique=True)
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



