from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app_cadastro.models import PerfilUsuario

class Command(BaseCommand):
    help = 'Criar perfis de usuarios que não existe'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'perfil'):
                PerfilUsuario.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS(f'Perfil criado com sucesso {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'Já existe esse perfil {user.username} '))