import django
import os

# Configure o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seu_projeto.settings")
django.setup()

from materias.models import Professor, Comentario, Resumo, Video, Atividade, Turma

# Deletar todos os registros de Comentario, Resumo, Video e Atividade
Comentario.objects.all().delete()
Resumo.objects.all().delete()
Video.objects.all().delete()
Atividade.objects.all().delete()

# Limpar os ManyToMany de Professor
for professor in Professor.objects.all():
    professor.aprovacoes.clear()

# Limpar os ManyToMany de Comentario (mesmo que os comentários foram deletados, para garantir)
for comentario in Comentario.objects.all():
    comentario.curtidas.clear()
    comentario.denuncia.clear()

# Limpar os ManyToMany de Resumo
for resumo in Resumo.objects.all():
    resumo.curtidas.clear()

# Limpar os ManyToMany de Video
for video in Video.objects.all():
    video.curtidas.clear()

# Limpar os ManyToMany de Atividade
for atividade in Atividade.objects.all():
    atividade.curtidas.clear()
    atividade.avaliadores.clear()

# Resetar campos de avaliação e limpar avaliadores das Turmas
for turma in Turma.objects.all():
    turma.numero_avaliacoes = 0
    turma.avaliacao_dificuldade = 0
    turma.avaliacao_apoio_aluno = 0
    turma.avaliacao_didatica = 0
    turma.avaliadores.clear()
    turma.save()

print("Dados relacionados zerados com sucesso, turmas intactas!")
