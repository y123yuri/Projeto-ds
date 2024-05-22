from django.shortcuts import render, HttpResponse, redirect
from .models import *
import time
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from datetime import timezone
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'UnBook.html')

def somos(request):
    return render(request, 'Quem_somos.html')

def tutorial(request):
    return render(request, 'Tutorial.html')

def perfil(request):
    return render(request, "html/Perfil.html")    

def pesquisa(request):
    termo_pesquisa = request.POST['termo_pesquisa']
    start_time = time.time()
    str_lista = Professor.objects.pesquisa(termo_pesquisa)
    obj_lista = []
    for nome in str_lista:
        prof_obj = Professor.objects.get(nome=nome)
        if Turma.objects.filter(professor=prof_obj):
            obj_lista.append(prof_obj)
        
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
    print(termo_pesquisa_materias)
    resposta = ''

    if len(obj_lista_materia)>0:
        resposta = obj_lista_materia[0].codigo+','+obj_lista_materia[0].nome
        if (len(obj_lista_materia)>1):
            for obj in obj_lista_materia[1:]:
                resposta += ";"+obj.codigo+','+obj.nome
    
    return HttpResponse(resposta)


def materia(request, codigo, nome):
    if request.user.is_authenticated:
        print(codigo, nome)
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_prof = Professor.objects.get(nome=nome)

        obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
        context = {}
        context["turma"] = obj_turma
        context["avaliacao_didatica"] = obj_turma.avaliacao_didatica/2
        context["avaliacao_dificuldade"] = obj_turma.avaliacao_dificuldade/2
        context["avaliacao_apoio"] = obj_turma.avaliacao_apoio_aluno/2

        context["total_avaliadores"] = obj_turma.avaliadores.count()
        context["comentarios"] = []
        for comentario in Comentario.objects.filter(turma=obj_turma):
            print(comentario)
            context["comentarios"].append(comentario)
        
        index =0
        lista_turno = obj_turma.turno.split(" ")
        dias = []
        print(obj_turma.turno)
        for turno in lista_turno:
            
            for i in range(len(turno)):
                if not turno[i].isdigit():
                    index = i
            
            if ("(" not in turno) and (")" not in turno) and ("/" not in turno) and '-' not in turno:

                for n in range(index):
                    if len(turno[index:])==5:
                        dia = turno[n]+turno[index:index+3]
                        dias.append(dia)
                        dia = turno[n]+turno[index] +turno[index+3:]
                        dias.append(dia)
                    else:
                        dia = turno[n]+turno[index:]
                        dias.append(dia)
                        
        context["dias"] =  dias
        
        

        return render(request, "materia.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)

def professor(request, nome):
    
    ob_prof = Professor.objects.get(nome=nome)
    lista_turma = Turma.objects.filter(professor=ob_prof)
    context = {}
    context["lista_turmas"] = list(lista_turma)
    context["nome"] = nome
    context["foto"] = ob_prof.foto
    aval_didatica = 0
    aval_apoio = 0
    aval_dificuldade = 0
    total = 0
    for turma in lista_turma:
        quant_avaliadores = turma.avaliadores.count()
        aval_apoio += turma.avaliacao_apoio_aluno * quant_avaliadores
        aval_dificuldade += turma.avaliacao_dificuldade * quant_avaliadores
        aval_didatica += turma.avaliacao_didatica * quant_avaliadores
        total += quant_avaliadores

    if total>0:
        context["aval_apoio"] = (aval_apoio //total)/2
        context["aval_dificuldade"] = (aval_dificuldade //total)/2
        context["aval_didatica"] = (aval_didatica //total)/2
        context["aprovacao"] = ((int(ob_prof.aprovacoes.count())*100)//total)
    else:
        context["aval_apoio"] = 0
        context["aval_dificuldade"] = 0
        context["aval_didatica"] = 0
        context["aprovacao"] = 0
    context["quant_aval"] = total

    return render(request, "Professor.html", context)
    

def pesquisa_turma(request):
    codigo = request.POST['codigo']
    materia = Materia.objects.get(codigo=codigo)
    lista_turmas = list(Turma.objects.filter(materia=materia))
    resposta = ''
    if len(lista_turmas)>0:
        resposta = lista_turmas[0].professor.foto+','+lista_turmas[0].professor.nome+','+lista_turmas[0].turno+','+lista_turmas[0].materia.codigo
        if (len(lista_turmas)>1):
            for obj in lista_turmas[1:]:
                resposta += ";"+obj.professor.foto+','+obj.professor.nome+','+obj.turno+','+obj.materia.codigo
    return HttpResponse(resposta)


def videos(request, nome,codigo) :
    if request.user.is_authenticated:
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_prof = Professor.objects.get(nome=nome)

        obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
        context = {}
        context["turma"] = obj_turma

        return render(request, "Videos.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)

def resumos(request, nome,codigo) :
    if request.user.is_authenticated:
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_prof = Professor.objects.get(nome=nome)

        obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
        context = {}
        context["turma"] = obj_turma

        return render(request, "Livros.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)

def atividades(request, nome,codigo) :
    if request.user.is_authenticated:
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_prof = Professor.objects.get(nome=nome)

        obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
        context = {}
        context["turma"] = obj_turma

        return render(request, "Atividades.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)


def avaliacao(request):
    # Obtenha os dados do POST
    lista = request.POST['avaliacao']
    codigo_materia = request.POST['materia']
    nome_prof = request.POST['professor']

    # Obtenha os objetos necessários
    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_prof = Professor.objects.get(nome=nome_prof)
    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)

    # Separe os dados da lista
    separacao = lista.split(',')

    dificuldade_dados = int(float(separacao[0])*2)  # Converta para float
    apoio_dados = int(float(separacao[1])*2)
    didatica_dados = int(float(separacao[2])*2)

    # Verifique se o usuário já avaliou esta turma
    user = request.user
    numero_avaliacoes = int(obj_turma.avaliadores.count())

    if user in obj_turma.avaliadores.all():
        # O usuário já avaliou, então precisamos subtrair sua avaliação anterior
        # Vamos buscar a avaliação anterior para subtrair
        avaliacao_anterior = obj_turma.avaliacao_dificuldade
        apoio_anterior = obj_turma.avaliacao_apoio_aluno
        didatica_anterior = obj_turma.avaliacao_didatica

        # Calcule as novas médias removendo a contribuição anterior e adicionando a nova
        nova_dificuldade = ((obj_turma.avaliacao_dificuldade * numero_avaliacoes) - avaliacao_anterior + dificuldade_dados) // numero_avaliacoes
        nova_apoio = ((obj_turma.avaliacao_apoio_aluno * numero_avaliacoes) - apoio_anterior + apoio_dados) // numero_avaliacoes
        nova_didatica = ((obj_turma.avaliacao_didatica * numero_avaliacoes) - didatica_anterior + didatica_dados) // numero_avaliacoes
        if user in obj_prof.aprovacoes.all() and not lista[3]:
            obj_prof.aprovacoes.remove(user)
    else:
        # O usuário não avaliou, então adicionamos a avaliação e incrementamos o contador
        numero_avaliacoes += 1

        # Calcule as novas médias incluindo a nova avaliação
        nova_dificuldade = ((obj_turma.avaliacao_dificuldade * (numero_avaliacoes - 1)) + dificuldade_dados) // numero_avaliacoes
        nova_apoio = ((obj_turma.avaliacao_apoio_aluno * (numero_avaliacoes - 1)) + apoio_dados) // numero_avaliacoes
        nova_didatica = ((obj_turma.avaliacao_didatica * (numero_avaliacoes - 1)) + didatica_dados) // numero_avaliacoes
        if user not in obj_prof.aprovacoes.all() and lista[3]:
            obj_prof.aprovacoes.add(user)

        # Adicione o usuário aos avaliadores
        obj_turma.avaliadores.add(user)

    # Atualize os campos com os novos valores
    obj_turma.avaliacao_dificuldade = nova_dificuldade
    obj_turma.avaliacao_apoio_aluno = nova_apoio
    obj_turma.avaliacao_didatica = nova_didatica
    obj_turma.numero_avaliacoes = numero_avaliacoes
    obj_turma.save()
    


    print(obj_turma.avaliacao_dificuldade)
    print(obj_turma.avaliacao_apoio_aluno)
    print(obj_turma.avaliacao_didatica)
    context = {}
    
    resposta_dificuldade = obj_turma.avaliacao_dificuldade
    resposta_apoio = obj_turma.avaliacao_apoio_aluno
    resposta_didatica = obj_turma.avaliacao_didatica
    
    
    context = {
        'avaliacao_dificuldade': resposta_dificuldade,
        'avaliacao_apoio_aluno': resposta_apoio,
        'avaliacao_didatica': resposta_didatica,
    }

    return HttpResponse(f'{resposta_dificuldade}, {resposta_apoio}, {resposta_didatica}')
    


def comentarios(request):
    comentario_usuario = request.POST['comentario']
    codigo_materia = request.POST['materia']
    nome_prof = request.POST['professor']

    # Obtenha os objetos necessários
    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_prof = Professor.objects.get(nome=nome_prof)
    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)

    user = request.user
    print(comentario_usuario)
    novo_comentario = Comentario(autor=user, hora_publicacao=timezone.now(), turma=obj_turma, texto=comentario_usuario)
    novo_comentario.save()
    return HttpResponse("ok")