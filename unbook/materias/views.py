from django.shortcuts import render, HttpResponse
from .models import *
import time

# Create your views here.

def home(request):
    return render(request, 'UnBook.html')

def somos(request):
    return render(request, 'Quem_somos.html')

def pesquisa(request):
    termo_pesquisa = request.POST['termo_pesquisa']
    start_time = time.time()
    str_lista = Professor.objects.pesquisa(termo_pesquisa)
    obj_lista = []
    for nome in str_lista:
        obj_lista.append(Professor.objects.get(nome=nome))
    
    for obj in obj_lista:
        turma = Turma.objects.filter(professor=obj)
        if not turma:
            obj_lista.remove(obj)
    print(f'termo de busca:{termo_pesquisa}')
    print("--- %s seconds ---" % (time.time() - start_time))
    
    resposta = ""
    if len(obj_lista)>0:
        resposta = obj_lista[0].nome+','+obj_lista[0].foto
        if (len(obj_lista)>1):
            for obj in obj_lista[1:]:
                resposta += ";"+obj.nome+','+obj.foto
    return HttpResponse(resposta)

def pesquisa_materias(request):
    termo_pesquisa_materias = request.POST['termo_pesquisa_materias']
    obj_lista_materia = Materia.objects.pesquisa(termo_pesquisa_materias)
    print(obj_lista_materia)
    resposta = ''

    if len(obj_lista_materia)>0:
        resposta = obj_lista_materia[0].codigo+','+obj_lista_materia[0].nome
        if (len(obj_lista_materia)>1):
            for obj in obj_lista_materia[1:]:
                resposta += ";"+obj.codigo+','+obj.nome
    
    return HttpResponse(resposta)

def materia(request, codigo, nome):
    print(codigo, nome)
    obj_materia = Materia.objects.get(codigo=codigo)
    obj_prof = Professor.objects.get(nome=nome)

    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
    context = {}
    context["turma"] = obj_turma

    return render(request, "materia.html", context)

def professor(request, nome):
    ob_prof = Professor.objects.get(nome=nome)
    lista_turma = Turma.objects.filter(professor=ob_prof)
    context = {}
    context["lista_turmas"] = list(lista_turma)
    context["nome"] = nome
    context["foto"] = ob_prof.foto
    aval_1 = 0
    aval_2 = 0
    aval_3 = 0
    for turma in lista_turma:
        aval_1 += turma.avaliação_1
        aval_2 += turma.avaliação_2
        aval_3 += turma.avaliação_3
    
    context["aval_1"] = aval_1 /len(lista_turma)
    context["aval_2"] = aval_2 /len(lista_turma)
    context["aval_3"] = aval_3 /len(lista_turma)

    return render(request, "Professor.html", context)


