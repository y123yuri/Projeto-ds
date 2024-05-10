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

def pesquisa_materias(request):
    termo_pesquisa_materias = request.POST['termo_pesquisa_materias']
    print(Materia.objects.pesquisa(termo_pesquisa_materias))
    obj_lista_materia = Materia.objects.pesquisa(termo_pesquisa_materias)
    resposta = ''

    if len(obj_lista_materia)>0:
        resposta = obj_lista_materia[0].codigo+','+obj_lista_materia[0].nome+','+obj_lista_materia[0].carga_horaria
        if (len(obj_lista_materia)>1):
            for obj in obj_lista_materia[1:]:
                resposta += ";"+obj.codigo+','+obj.nome+';'+obj.carga_horaria
            
    return HttpResponse(resposta)

def materia(request, codigo, nome):
    print(codigo, nome)
    obj_materia = Materia.objects.get(codigo=codigo)
    obj_prof = Professor.objects.get(nome=nome)

    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
    context = {}
    context["turma"] = obj_turma
    return render(request, "materia.html", context)
