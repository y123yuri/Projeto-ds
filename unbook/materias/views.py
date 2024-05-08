from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'UnBook.html', {})

def somos(request):
    return render(request, 'Quem_somos.html')

def pesquisa(request):
    termo_pesquisa = request.POST['termo_pesquisa']
    print(Professor.objects.pesquisa(termo_pesquisa))
    obj_lista = Professor.objects.pesquisa(termo_pesquisa)
    resposta = ""
    if len(obj_lista)>0:
        resposta = obj_lista[0].nome+','+obj_lista[0].foto
        if (len(obj_lista)>1):
            for obj in obj_lista[1:]:
                resposta += ";"+obj.nome+','+obj.foto
    return HttpResponse(resposta)

def pesquisa_turma(request):
    termo_pesquisa_materia = request.POST['termo_pesquisa_materia']
    print(Materia.objects.pesquisa(termo_pesquisa_materia))
    obj_lista_materia = Materia.objects.pesquisa(termo_pesquisa_materia)
    resposta2 = ''
    if len(obj_lista_materia)>0:
        resposta = obj_lista_materia[0].codigo+','+obj_lista_materia.nome[0]+','+obj_lista_materia.carga_horaria[0]
        if (len(obj_lista_materia)>2):
            for obj in obj_lista_materia[1:]:
                resposta_materia += ";"+obj.codigo+','+obj.nome+';'+obj.carga_horaria
        return HttpResponse(resposta_materia)
