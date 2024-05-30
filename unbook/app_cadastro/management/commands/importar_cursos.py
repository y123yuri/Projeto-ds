from django.core.management.base import BaseCommand
from app_cadastro.models import Cursos_unb
import os

class Command(BaseCommand):
    help = 'Importa cursos de um arquivo txt'

    def handle(self, *args, **kwargs):
        # Defina o caminho para o arquivo cursos.txt
        caminho_arquivo = os.path.join('data', 'lista_espaco.txt')

        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                cursos = file.readlines()
            
            for nome in cursos:
                nome = nome.strip()
                nome = nome.replace("['", '')
                nome = nome.replace("']",'') # Remove espaços em branco ao redor do texto
                if nome:  # Certifica-se de que não é uma linha vazia
                    Cursos_unb.objects.get_or_create(curso=nome)
                    self.stdout.write(self.style.SUCCESS(f'Curso "{nome}" importado com sucesso'))

            self.stdout.write(self.style.SUCCESS('Todos os cursos foram importados!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'O arquivo {caminho_arquivo} não foi encontrado.'))