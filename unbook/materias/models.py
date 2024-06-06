from django.db import models
from unidecode import unidecode
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class ProfessorManager(models.Manager):
    def pesquisa(self, termo_busca):
        encontrado = []
        for obj in super().get_queryset().values_list('nome', flat=True):
            nome_sem_acento = unidecode(obj)
            lista_nome = obj.split()
            for nome in lista_nome:
                index = obj.index(nome)
                if obj[index:index+len(termo_busca)] == termo_busca or nome_sem_acento[index:index+len(termo_busca)] == termo_busca:
                    encontrado.append(obj)
                    break
        return encontrado


class MateriaManager(models.Manager):
     def pesquisa(self, termo_busca):
        
        encontrado = []
        for obj in super().get_queryset().iterator():
            nome_sem_acento = unidecode(obj.nome)
            lista_materia = obj.nome.split()
            for nome in lista_materia:
                index = obj.nome.index(nome)
                if obj.nome[index:index+len(termo_busca)] == termo_busca or nome_sem_acento[index:index+len(termo_busca)] == termo_busca:
                    encontrado.append(obj)
                    break
                elif obj.codigo[:len(termo_busca)] == termo_busca:
                    encontrado.append(obj)
                    break
        return encontrado
                

class Professor(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    foto = models.URLField()
    objects = ProfessorManager()
    aprovacoes = models.ManyToManyField(settings.AUTH_USER_MODEL ,default=None)
    

    def __str__(self):
        return self.nome




class Materia(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=100)
    objects = MateriaManager()

    def __str__(self):
        return self.codigo + " " + self.nome + " "
    

class Comentario(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    hora_publicacao = models.DateTimeField()
    texto = models.CharField(max_length=250)
    curtidas = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="curtida")
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE, default=None)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.ativo} : {self.hora_publicacao}: {self.autor} : {self.texto}'

class Comentario_deletado(models.Model):
    autor = models.CharField(max_length=50)
    dia = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    texto = models.CharField(max_length=250)
    

    def __str__(self):
        return f' {self.autor} : {self.texto}'
    

class Turma(models.Model):
    professor = models.ForeignKey("Professor", on_delete=models.CASCADE)
    materia = models.ForeignKey("Materia", on_delete=models.CASCADE)
    turno = models.CharField(max_length=30, default="NA")
    local = models.CharField(max_length=30, default="NA")
    
    numero_avaliacoes = models.PositiveIntegerField(default=0)

    avaliacao_dificuldade = models.IntegerField(default=0)
    avaliacao_apoio_aluno = models.IntegerField(default=0)
    avaliacao_didatica = models.IntegerField(default=0)

    avaliadores = models.ManyToManyField(settings.AUTH_USER_MODEL, default=None)

    def __str__(self):
        return self.materia.codigo + "/" + self.professor.nome

class Report(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    cont_ofensivo = models.BooleanField()
    info_falsa = models.BooleanField()
    bullying = models.BooleanField()
    cont_sexual = models.BooleanField()
    discurso_odio = models.BooleanField()
    observacao = models.CharField(max_length=250)
    hora_publicacao = models.DateTimeField()
    def __str__(self):
        return  self.autor.username + ' ' + '/' + ' ' + self.comentario.texto  + '/' + self.observacao


class Resumo(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    hora_publicacao = models.DateTimeField()
    titulo = models.CharField(max_length=60)
    link = models.CharField(max_length=250)
    curtidas = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="curtida_resumo")
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE, default=None)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.ativo} : {self.titulo} : {self.autor}'



class Video(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    hora_publicacao = models.DateTimeField()
    titulo = models.CharField(max_length=60)
    link = models.CharField(max_length=250)
    curtidas = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="curtida_videos")
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE, default=None)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.ativo} : {self.titulo} : {self.autor}'

class Atividade(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    hora_publicacao = models.DateTimeField()
    titulo = models.CharField(max_length=60)
    link = models.CharField(max_length=250)
    curtidas = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="curtida_atividades")
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE, default=None)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.ativo} : {self.titulo} : {self.autor}'