from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    foto = models.URLField()

    def __str__(self):
        return self.nome


class Materia(models.Model):
    codigo = models.CharField(max_length=9, primary_key=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=10)
    def __str__(self):
        return self.codigo + " " + self.nome


class Comentario(models.Model):
    autor_nick = models.CharField(max_length=100)
    autor_email = models.EmailField()
    hora_publicacao = models.TimeField()
    texto = models.CharField(max_length=250)
    curtidas = models.IntegerField()

class Turma(models.Model):
    professor = models.ForeignKey("Professor", on_delete=models.CASCADE)
    materia = models.ForeignKey("Materia", on_delete=models.CASCADE)
    # comentario = models.ForeignKey(Comentario)
    avaliação_1 = models.FloatField()
    avaliação_2 = models.FloatField()
    avaliação_3 = models.FloatField()
    def __str__(self):
        return self.materia.codigo + "/" + self.professor.nome



