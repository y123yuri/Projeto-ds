from django.db import models

# Create your models here.

class Cadastro(models.Model):
    username = models.CharField(max_length=150, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=22, null=False, blank=False, unique=True, primary_key=True)
    password = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.email}: {self.username}'