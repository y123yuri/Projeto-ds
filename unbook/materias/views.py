from django.shortcuts import render, HttpResponse, redirect
from .models import *
import time
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from datetime import timezone
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
from django.views.decorators.http import require_http_methods
from .models import Comentario
from .models import Comentario_deletado
from django.http import JsonResponse
from django.contrib import messages
from app_cadastro.models import PerfilUsuario
from django.shortcuts import get_object_or_404
import re
import os

SEMESTRE_ATUAL = "2024.2"

# Create your views here.

#apagar a minha conta nesse caraio - Schneider
# def deletar_conta_email(request, email):
#     user = get_object_or_404(User, email=email)
#     user.delete()
#     print('schneider é gay')
#     return redirect('')

def home(request):
    user= request.user
    if request.user.is_authenticated:
        perfil_existente = PerfilUsuario.objects.filter(user=user).first()
        context = {
            'perfil': perfil_existente,
            'semestre': SEMESTRE_ATUAL
            }
        return render(request, 'UnBook.html', context)
    else: 
        pass
        return render(request, 'UnBook.html')

def somos(request):
    return render(request, 'qmsomos.html')


def tutorial(request):
    return render(request, 'Tutorial.html')

def perfil(request):
    return render(request, "html/Perfil.html")    

def feedback(request):
    return render(request, "feedback.html")

def enviar_feedback(request):
    titulo = str(datetime.now())
    titulo += "_"+ request.POST["titulo"].strip().capitalize()
    caminho = os.path.join(os.path.dirname("/home/ubuntu/feedback"), f'{titulo}.txt')
    titulo = titulo.replace(" ", "_")
    corpo = request.POST["corpo"]
        
    print('-='*25)
    print(titulo)
    print('--'*25)
    print(corpo)
    
    with open(caminho, "w") as fp: #
        fp.write(corpo)
    
    return HttpResponse("enviado")

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
    # print(obj_lista_materia)
    # print(termo_pesquisa_materias)
    resposta = ''

    if len(obj_lista_materia)>0:
        resposta = obj_lista_materia[0].codigo+','+obj_lista_materia[0].nome
        if (len(obj_lista_materia)>1):
            for obj in obj_lista_materia[1:]:
                resposta += ";"+obj.codigo+','+obj.nome
    
    return HttpResponse(resposta)


def materia(request, semestre, codigo, nome):
    nomes = nome.split("$")
    lista_posicao = []
    context = {
        "semestre": semestre
    }
    cont = 0
    if request.user.is_authenticated:
        # print(codigo, nome)
        obj_materia = Materia.objects.get(codigo=codigo)
        professores = []
        for n in nomes:
            obj_prof = Professor.objects.get(nome=n)
            professores.append(obj_prof)
        
        obj_turma = Turma.objects.filter(materia=obj_materia)
        for prof in professores:
            obj_turma = obj_turma.filter(professor=prof)
        if len(obj_turma.all())>1:
            for obj in obj_turma.all():
                if len(nomes) == len(obj.professor.all()):
                    obj_turma = obj
                    break
        else:
            obj_turma = obj_turma.get()
        
        obj_semestre = Info_semestre.objects.get(turma=obj_turma, semestre=semestre)
        

        

  ##puxar pelo id da turma
            
        context["turma"] = obj_turma
        context["avaliacao_didatica"] = obj_turma.avaliacao_didatica/2
        context["avaliacao_dificuldade"] = obj_turma.avaliacao_dificuldade/2
        context["avaliacao_apoio"] = obj_turma.avaliacao_apoio_aluno/2

        context["total_avaliadores"] = obj_turma.avaliadores.count()
        context["comentarios"] = []
        context["quant_like"] = []
        context["curtidas"] = []
        context["professor"] = []
        for prof in obj_turma.professor.all():
            context["professor"].append(prof)
    
        
        context["professor_unico"] = nome
       #puxar o professor que bnao da duas aulas da mesma turma

        pre_context = []
        pre_context_curtida = []
        contador_comentario = 0 

        
        lista_context_comentario = []
        lista_context_curtida=[]

        context_comentario_final = []
        context_curtida_final= []

        lista_tudao = []
        contador_true = 0
        lista_curtidas = []
        lista_fodase  = []
        
        
        for comentario in Comentario.objects.filter(turma=obj_turma):
            if comentario.ativo: 
                pre_context.append(comentario)
                pre_context_curtida.append(comentario.curtidas.count())

                
                if comentario.curtidas.filter(id=request.user.id).exists():
                    comentario = str(comentario)
                    comentario_divisao = comentario.split(":")
                    
                    comentario_id = comentario_divisao[0]+"C" #para diferenciar dos não curtidos
                    lista_curtidas.append(comentario_id)
                else:
                    comentario = str(comentario)
                    comentario_divisao = comentario.split(":")
                    
                    comentario_id = comentario_divisao[0]
                    lista_curtidas.append(comentario_id)
                
###########################################
                
       

                
#################################################
        for c in range(0,len(pre_context_curtida)): #deixa os cometarios em ordem
            nova = [pre_context[c]],[pre_context_curtida[c]]
            lista_tudao.append(nova)
        
        nova_lista = sorted(lista_tudao, key=lambda lista_tudao:lista_tudao[1], reverse=True) ######### deixa em ordem

    
        for c in nova_lista:
            
            comentarios_nova_lista=c[0] #####comentario
            curtidas_nova_lista=c[1] ###comentario curtida
            
            context_comentario_final.append(comentarios_nova_lista)
            context_curtida_final.append(curtidas_nova_lista)
            if c[0][0].curtidas.filter(id=request.user.id).exists():
                context["curtidas"].append(True)
            else:
                context["curtidas"].append(False)
                
        
        for d in context_comentario_final:
            x= d[0]
            context["comentarios"].append(x) ####context com a ordem certa somente dos comentarios

        for e in context_curtida_final:
            x= e[0]
            context["quant_like"].append(x) ### context com as curtidas dos comentários em ordem

####################################################   CALENDARIO     
        index =0
        lista_turno = obj_semestre.turno.split(" ")
        dias = []
        
        # print(obj_turma.turno)
        for turno in lista_turno: #processa cada turno separado
            #tamanho do turno
            for i in range(len(turno)): # ler cada digito do turno
                if not turno[i].isdigit():
                    index = i  ### manha tarde ou noite, posicao onde esta a letra
                    arg = index + 1
            if ("(" not in turno) and (")" not in turno) and ("/" not in turno) and '-' not in turno:
#
                for n in range(index): ###  pegar dia da semana
                    arg = index + 1
                    tamanho = len(turno)
                    if tamanho >= 4: #horaio diferente e dia diferent
                        for i in range(len(turno[index:])+1):
                            try:
                                dia = turno[n]+turno[index]+turno[arg]
                                arg += 1
                                dias.append(dia)
                            except IndexError:
                                print(' ')
                                
                    else: #mesmo horario porem dias diferentes
                        dia = turno[n]+turno[index:]
                        dias.append(dia)
            
            else: #para estagios com filtro fodido
                print('')
        
        print(dias)
        
        if obj_turma.avaliadores.filter(id=request.user.id).exists():
            context['materia_votou'] = 'sim'
            print(context['materia_votou'])
        else:
            pass
            
        #enviar
        context["dias"] =  dias
        print(context['dias'])
        

        return render(request, "materia.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../../cadastro/login', context)

def professor(request, nome):
    
    ob_prof = Professor.objects.get(nome=nome)
    lista_turma = Turma.objects.filter(professor=ob_prof)

    context = {}
    context["semestre"] = SEMESTRE_ATUAL #semestre atual
    context["lista_turmas"] = []
    lista_infos_semestre =  []
    context["professores"] = []

    for t in lista_turma:
        
        busca_info = list(Info_semestre.objects.filter(turma=t.id))
        for e in range(len(busca_info)):
            context["lista_turmas"].append(t)
            lista_prof = t.professor.all()[0].nome
            for prof in t.professor.all()[1:]:
                lista_prof += "$"+prof.nome
            context["professores"].append(lista_prof)
        
        lista_infos_semestre += busca_info
        print(lista_infos_semestre)
    
    context["info_semestre"] =  lista_infos_semestre

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
        infos = list(Info_semestre.objects.filter(turma=lista_turmas[0]))
        
        for info in infos:
            if info == infos[0]:
                resposta = lista_turmas[0].professor.all()[0].foto
                for prof in lista_turmas[0].professor.all()[1:]:
                    resposta += "$"+prof.foto
                resposta += ','+lista_turmas[0].professor.all()[0].nome
                for prof in lista_turmas[0].professor.all()[1:]:
                    resposta += "$"+prof.nome
                resposta += ','+info.turno+','+lista_turmas[0].materia.codigo+','+info.semestre
            else:
                resposta +=  ";"+lista_turmas[0].professor.all()[0].foto
                for prof in lista_turmas[0].professor.all()[1:]:
                    resposta += "$"+prof.foto
                resposta += ','+lista_turmas[0].professor.all()[0].nome
                for prof in lista_turmas[0].professor.all()[1:]:
                    resposta += "$"+prof.nome
                resposta += ','+info.turno+','+lista_turmas[0].materia.codigo+','+info.semestre
        
        
        if (len(lista_turmas)>1):
            for obj in lista_turmas[1:]:
                
                infos = list(Info_semestre.objects.filter(turma=obj))
                
                for info in infos:
                    print(info.semestre)
                    resposta +=  ";"+obj.professor.all()[0].foto
                    for prof in obj.professor.all()[1:]:
                        resposta += "$"+prof.foto
                    resposta += ','+obj.professor.all()[0].nome
                    for prof in obj.professor.all()[1:]:
                        resposta += "$"+prof.nome
                    resposta += ','+info.turno+','+obj.materia.codigo+','+info.semestre
            
    return HttpResponse(resposta)


def videos(request, semestre, nome, codigo) :
    nomes = nome.split("$")
    if request.user.is_authenticated:
        
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_profs = []
        for n in nomes:
            obj_profs.append(Professor.objects.get(nome=n))
        obj_turma = Turma.objects.filter(materia=obj_materia)
        for prof in obj_profs:
            obj_turma = obj_turma.filter(professor=prof)
        if len(obj_turma.all())>1:
            for obj in obj_turma.all():
                if len(nomes) == len(obj.professor.all()):
                    obj_turma = obj
                    break
        else:
            obj_turma = obj_turma.get()
        
        context = {}
        context["turma"] = obj_turma
        context["semestre"] = semestre
        context["professor_link"] = obj_profs[0].nome
        for p in obj_profs[1:]:
            context["professor_link"] += "$"+p.nome
        context["professor"] = obj_profs

        lista_videos = []
        lista_quant_curtida = []
        lista_bool_curtiu = []

        for video in Video.objects.filter(turma=obj_turma):
            lista_videos.append(video)
            lista_quant_curtida.append(video.curtidas.count())
            lista_bool_curtiu.append( 1 if video.curtidas.filter(id=request.user.id).exists() else 0)

        # dps implementar ordenação em uma FUNÇÃO
        print(lista_bool_curtiu)
        context["videos"] = lista_videos
        context["bool_curtiu"] = lista_bool_curtiu
        context["quant_curtidas"] = lista_quant_curtida


        return render(request, "Videos.html", context)
    
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)

def atividades(request, semestre, nome, codigo) :
    nomes = nome.split("$")
    if request.user.is_authenticated:
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_profs = []
        for n in nomes:
            obj_profs.append(Professor.objects.get(nome=n))
        obj_turma = Turma.objects.filter(materia=obj_materia)
        for prof in obj_profs:
            obj_turma = obj_turma.filter(professor=prof)
        if len(obj_turma.all())>1:
            for obj in obj_turma.all():
                if len(nomes) == len(obj.professor.all()):
                    obj_turma = obj
                    break
        else:
            obj_turma = obj_turma.get()

        context = {}

        context["turma"] = obj_turma
        context["semestre"] = semestre
        context["professor_link"] = obj_profs[0].nome
        for p in obj_profs[1:]:
            context["professor_link"] += "$"+p.nome
        context["professor"] = obj_profs

        lista_atividades = []
        lista_quant_curtida = []
        lista_bool_curtiu = []

        for atividade in Atividade.objects.filter(turma=obj_turma):
            lista_atividades.append(atividade)
            lista_quant_curtida.append(atividade.curtidas.count())
            lista_bool_curtiu.append( 1 if atividade.curtidas.filter(id=request.user.id).exists() else 0)

        # dps implementar ordenação em uma FUNÇÃO
        print(lista_bool_curtiu)
        
        context["atividades"] = lista_atividades
        context["bool_curtiu"] = lista_bool_curtiu
        context["quant_curtidas"] = lista_quant_curtida

        return render(request, "Atividades.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)

def resumos(request, semestre, nome,codigo):
    nomes = nome.split("$")
    if request.user.is_authenticated:
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_profs = []
        for n in nomes:
            obj_profs.append(Professor.objects.get(nome=n))
        obj_turma = Turma.objects.filter(materia=obj_materia)
        for prof in obj_profs:
            obj_turma = obj_turma.filter(professor=prof)
        if len(obj_turma.all())>1:
                for obj in obj_turma.all():
                    if len(nomes) == len(obj.professor.all()):
                        obj_turma = obj
                        break
        else:
            obj_turma = obj_turma.get()

        context = {}

        context["turma"] = obj_turma
        context["semestre"] = semestre
        context["professor_link"] = obj_profs[0].nome
        for p in obj_profs[1:]:
            context["professor_link"] += "$"+p.nome
        context["professor"] = obj_profs


        lista_resumos = []
        lista_quant_curtida = []
        lista_bool_curtiu = []
        for resumo in Resumo.objects.filter(turma=obj_turma):
            lista_resumos.append(resumo)
            lista_quant_curtida.append(resumo.curtidas.count())
            lista_bool_curtiu.append( 1 if resumo.curtidas.filter(id=request.user.id).exists() else 0)

        # dps implementar ordenação em uma FUNÇÃO

        context["resumos"] = lista_resumos
        context["bool_curtiu"] = lista_bool_curtiu
        context["quant_curtidas"] = lista_quant_curtida

        return render(request, "Livros.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)


        
def add_video(request): #ajax function
    codigo_materia = request.POST["materia"]

    nomes = request.POST["professor"].split("$")

    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_profs = []
    for n in nomes:
        print(n)
        obj_profs.append(Professor.objects.get(nome=n))
    obj_turma = Turma.objects.filter(materia=obj_materia)
    for prof in obj_profs:
        obj_turma = obj_turma.filter(professor=prof)
    if len(obj_turma.all())>1:
            for obj in obj_turma.all():
                if len(nomes) == len(obj.professor.all()):
                    obj_turma = obj
                    break
    else:
        obj_turma = obj_turma.get()


    nome_link = request.POST["titulo"]

    link = request.POST["link"].replace("https://", "").replace("www.", "")
    print(f"link: {link}; nome:{nome_link} video")
    if link[:11] == "youtube.com" or link[:16] == "drive.google.com":
        #filtro de videos
        if not Video.objects.filter(link=link,turma=obj_turma).exists() :
            print("oi")
            video = Video(
                turma=obj_turma,
                hora_publicacao=timezone.now(),
                titulo=nome_link,
                link=link,
                autor=request.user)
            video.save()
            return HttpResponse("ok")
        else:
            messages.error(request, 'O link postado já existe ou é inválido.')
            return HttpResponse("ok")
        return HttpResponse("erro")
    else:
        return HttpResponse("erro")

def like_video(request):
    id = request.POST["id_video"]
    video = Video.objects.get(id=id)
    print(video.titulo)
    if video.curtidas.filter(id=request.user.id).exists():
        print("vou remover o user")
        video.curtidas.remove(request.user)
        return HttpResponse("remove")
    else:
        print("vou adicionar o user")
        video.curtidas.add(request.user)
        return HttpResponse("add")
    
    





def add_resumo(request): #ajax function
    codigo_materia = request.POST["materia"]

    nomes = request.POST["professor"]
    lista_professores = nomes.strip('[]').split(', ')

    nomes_formatados = [prof.replace('&lt;Professor: ', '').replace('&gt;', '').strip() for prof in lista_professores]

    print(nomes_formatados)

    obj_materia = Materia.objects.get(codigo=codigo_materia)
    
    obj_profs = []

    for n in nomes_formatados:
        obj_profs.append(Professor.objects.get(nome=n))
    obj_turma = Turma.objects.filter(materia=obj_materia)
    for prof in obj_profs:
        obj_turma = obj_turma.filter(professor=prof)
    if len(obj_turma.all())>1:
            for obj in obj_turma.all():
                if len(nomes) == len(obj.professor.all()):
                    obj_turma = obj
                    break
    else:
        obj_turma = obj_turma.get()


    nome_link = request.POST["titulo"]
    link = request.POST["link"].replace("https://", "").replace("www.", "")
    
    print(f"link: {link}; nome:{nome_link} resumo")
    if link[:11] == "youtube.com" or link[:16] == "drive.google.com" or link[:15] =='docs.google.com' or link[:19] == 'teams.microsoft.com' or link[:7] == '1drv.ms':
        print(link, "link")
        #filtro de resumo
        if not Resumo.objects.filter(link=link, turma=obj_turma).exists():
            print("oi")
            resumo = Resumo(
                turma=obj_turma,
                hora_publicacao=timezone.now(),
                titulo=nome_link,
                link=link,
                autor=request.user)
            resumo.save()
            return HttpResponse("ok")
        else:
            messages.error(request, 'O link postado já existe ou é inválido.')
            return HttpResponse("ok")
    else:
        print("Link não adequado")
        return HttpResponse("erro")

def like_resumo(request):
    id = request.POST["id_resumo"]
    resumo = Resumo.objects.get(id=id)
    print(resumo.titulo)
    if resumo.curtidas.filter(id=request.user.id).exists():
        print("vou remover o user")
        resumo.curtidas.remove(request.user)
        return HttpResponse("remove")
    else:
        print("vou adicionar o user")
        resumo.curtidas.add(request.user)
        return HttpResponse("add")




def add_atividade(request):
    codigo_materia = request.POST["materia"]

    nomes = request.POST["professor"].split("$")

    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_profs = []
    for n in nomes:
        print(n)
        obj_profs.append(Professor.objects.get(nome=n))
    obj_turma = Turma.objects.filter(materia=obj_materia)
    for prof in obj_profs:
        obj_turma = obj_turma.filter(professor=prof)
    if len(obj_turma.all())>1:
            for obj in obj_turma.all():
                if len(nomes) == len(obj.professor.all()):
                    obj_turma = obj
                    break
    else:
        obj_turma = obj_turma.get()


    nome_link = request.POST["titulo"]
    link = request.POST["link"].replace("https://", "").replace("www.", "")
    context = {}
    print(f"link: {link}; nome:{nome_link} atividade")
    if link[:11] == "youtube.com" or link[:16] == "drive.google.com":
        #filtro de atividade
        if not Atividade.objects.filter(link=link,turma=obj_turma).exists():
            print("oi")
            atividade = Atividade(
                turma=obj_turma,
                hora_publicacao=timezone.now(),
                titulo=nome_link,
                link=link,
                autor=request.user)
            atividade.save()
            return HttpResponse("ok")
        else:
            messages.error(request, 'O link postado já existe ou é inválido.')
            return HttpResponse("ok")
            # return redirect('atividades')
    else:
        return HttpResponse("erro")

    
    
    
def avaliacao(request):
    # Obtenha os dados do POST
    lista = request.POST['avaliacao']
    codigo_materia = request.POST['materia']
    nomes_prof = request.POST['professor'].split(',')[:-1]
    print(nomes_prof)

    # Obtenha os objetos necessários
    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_profs = []
    obj_turma = Turma.objects.filter(materia=obj_materia)
    for nome in nomes_prof:
        obj_prof = Professor.objects.get(nome=nome)
        obj_profs.append(obj_prof)
        obj_turma = obj_turma.filter(professor=obj_prof)
    obj_turma = obj_turma.get()

    # Separe os dados da lista
    lista_gorda = []
    separacao = lista.split(',')
    
    cont_ava= 0
    for i in separacao:
        if i == '':
            print('porra') 
            x='0'
            lista_gorda.append(x)
        else:
            lista_gorda.append(i)
        cont_ava += 1
    print(lista_gorda)
    dificuldade_dados = int(float(lista_gorda[0])*2)  # Converta para float
    apoio_dados = int(float(lista_gorda[1])*2)
    didatica_dados = int(float(lista_gorda[2])*2)
    try:
        joinha = int(lista_gorda[3])
    except:
        joinha = 0
    
    
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
        for prof in obj_profs:
            if user in prof.aprovacoes.all():
                if joinha == 0 :
                    prof.aprovacoes.remove(user)
                    print(f"+1 reprovacao {prof}")
            else:
                prof.aprovacoes.add(user)
                print(f"+1 aprovação {prof}")
    else:
        # O usuário não avaliou, então adicionamos a avaliação e incrementamos o contador
        numero_avaliacoes += 1

        # Calcule as novas médias incluindo a nova avaliação
        nova_dificuldade = ((obj_turma.avaliacao_dificuldade * (numero_avaliacoes - 1)) + dificuldade_dados) // numero_avaliacoes
        nova_apoio = ((obj_turma.avaliacao_apoio_aluno * (numero_avaliacoes - 1)) + apoio_dados) // numero_avaliacoes
        nova_didatica = ((obj_turma.avaliacao_didatica * (numero_avaliacoes - 1)) + didatica_dados) // numero_avaliacoes
        for prof in obj_profs:
            if user not in prof.aprovacoes.all():
                if joinha == 1 :
                    prof.aprovacoes.add(user)
                    print(f"+1 aprovação {prof}")


        # Adicione o usuário aos avaliadores
        obj_turma.avaliadores.add(user)

    # Atualize os campos com os novos valores
    obj_turma.avaliacao_dificuldade = nova_dificuldade
    obj_turma.avaliacao_apoio_aluno = nova_apoio
    obj_turma.avaliacao_didatica = nova_didatica
    obj_turma.numero_avaliacoes = numero_avaliacoes
    obj_turma.save()
    


    # print(obj_turma.avaliacao_dificuldade)
    # print(obj_turma.avaliacao_apoio_aluno)
    # print(obj_turma.avaliacao_didatica)
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
    
def filtro(mensagem): #filtro é uma função separada que pode ser reutilizada em qualquer outro função
    lista_proibida = ['merda', 'porra', 'caralho', 'buceta', 'puta', 'foda se', 'cacete', 'desgraça', 'vagabunda', 'puta', 'arrombada', 'viado', 'cu', 'pau no cu', 'piranha', 'puta que pariu', 'puta merda', 'pqp', 'babaca', 'cuzão', 'escroto', 'fdp', 'bosta', 'fudido', 'caralha', 'corno', 'fudido', 'retardado', 'biscate', 'bicha', 'boquete', 'vagabundo', 'meretriz', 'arrombada', 'boiola', 'cabrão', 'chupa', 'escrota', 'trouxa', 'otário', 'xota', 'xoxota', 'zorra', 'cabrona', 'puta que te pariu', 'caralho de asa', 'puta', 'cornudo', 'caralhudo', 'escrotão', 'fode', 'maldito', 'jumento', 'panaca', 'retardado', 'paspalho', 'mané', 'boceta', 'trouxa', 'besta', 'ralé', 'meretriz', 'chupa rola', 'rola', 'puta velha', 'chifrudo', 'bostinha', 'merdinha', 'cagão', 'boiolinha', 'lixo', 'merdoso', 'bundão', 'lambisgóia', 'fedido', 'pau mole', 'pinto', 'pintudo', 'rabo', 'rabo de saia', 'safado', 'sem-vergonha', 'vagaba', 'bobo da corte', 'espermatozóide', 'cuspidor', 'coxinha', 'cabaço', 'fedorento', 'peido', 'peidão', 'vagabundinho', 'esquema', 'casca de ferida', 'bagulho', 'mentecapto', 'caga-regra', 'saco', 'saco cheio', 'capeta', 'inferno', 'tornozelo', 'babaca', 'panaca', 'fela da puta', 'fuder', 'velha', 'foder', 'sexo', 'fds', 'africano', 'aleijado', 'analfabeto', 'anus', 'anão', 'apenado', 'baba-ovo', 'babaca', 'babaovo', 'bacura', 'bagos', 'baianada', 'baitola', 'barbeiro', 'barraco', 'beata', 'bebum', 'besta', 'bicha', 'bisca', 'bixa', 'boazuda', 'boceta', 'boco', 'boiola', 'bolagato', 'bolcat', 'boquete', 'bosseta', 'bosta', 'bostana', 'branquelo', 'brecha', 'brexa', 'brioco', 'bronha', 'buca', 'buceta', 'bugre', 'bunda', 'bunduda', 'burra', 'burro', 'busseta', 'bárbaro', 'bêbado', 'cachorra', 'cachorro', 'cadela', 'caga', 'cagado', 'cagao', 'cagona', 'caipira', 'canalha', 'canceroso', 'caralho', 'casseta', 'cassete', 'ceguinho', 'checheca', 'chereca', 'chibumba', 'chibumbo', 'chifruda', 'chifrudo', 'chochota', 'chota', 'chupada', 'chupado', 'ciganos', 'clitoris', 'cocaina', 'coco', 
    'comunista', 'corna', 'corno', 'cornuda', 'cornudo', 'corrupta', 'corrupto', 'coxo', 'cretina', 'cretino', 'crioulo', 'cruz-credo', 'cu', 'culhao', 'curalho', 'cuzao', 'cuzuda', 'cuzudo', 'debil', 'debiloide', 'deficiente', 'defunto', 'demonio', 'denegrir', 'detento', 'difunto', 'doida', 'doido', 'egua', 'elemento', 'encostado', 'esclerosado', 'escrota', 'escroto', 'esporrada', 'esporrado', 'esporro', 'estupida', 'estupidez', 'estupido', 'fanático', 'fascista', 'fedida', 'fedido', 'fedor', 'fedorenta', 'feia', 'feio', 'feiosa', 'feioso', 'feioza', 'feiozo', 'felacao', 'fenda', 'fode', 'fodida', 'fodido', 'fornica', 'fornição', 'fudendo', 'fudeção', 'fudida', 'fudido', 'furada', 'furado', 'furnica', 'furnicar', 'furo', 'furona', 'furão', 'gaiata', 'gaiato','gilete', 'goianada', 'gonorrea', 'gonorreia', 'gosmenta', 
    'gosmento', 'grelinho', 'grelo', 'homo-sexual', 'homossexual', 'homossexualismo', 'idiota', 'idiotice', 'imbecil', 'inculto', 'iscrota', 'iscroto', 'judiar', 'ladra', 'ladrao', 'ladroeira', 'ladrona', 'ladrão', 'lalau', 'lazarento', 'leprosa', 'leproso', 'louco', 'lésbica', 'macaca', 'macaco', 'machona', 'macumbeiro', 'malandro', 'maluco', 'maneta', 'marginal', 'masturba', 'meleca', 'meliante', 'merda', 'mija', 'mijada', 'mijado', 'mijo', 'minorias', 'mocrea', 'mocreia', 'moleca', 'moleque', 'mondronga', 'mondrongo', 'mongol', 'mulato', 'naba', 'nadega', 'nazista', 'negro', 'nojeira', 'nojenta', 'nojento', 'nojo', 'olhota', 'otaria', 'otario', 'otária', 
    'otário', 'paca', 'palhaço', 'paspalha', 'paspalhao', 'paspalho', 'pau', 'peia', 'peido', 'pemba', 'pentelha', 'pentelho', 'perereca', 'perneta', 'peru', 'peão', 'pica', 
    'picao', 'pilantra', 'pinel', 'piranha', 'piroca', 'piroco', 'piru', 'pivete', 'político', 'porra', 'prega', 'preso', 'prost-bulo', 'prostibulo', 'prostituta', 'prostituto', 'punheta', 'punhetao', 'pus', 'pustula', 'puta', 'puto', 'puxa-saco', 'puxasaco', 'pênis', 'rabao', 'rabo', 'rabuda', 'rabudao', 'rabudo', 'rabudona', 'racha', 'rachada', 'rachadao', 'rachadinha', 'rachadinho', 'rachado', 'ramela', 'remela', 'retardada', 'retardado', 'roceiro', 'rola', 'rolinha', 'rosca', 'sacana', 'safada', 'safado', 'sapatao', 'sapatão', 'sifilis', 'siririca', 'tarada', 'tarado', 'tesuda', 'tezao', 'tezuda', 'tezudo', 'traveco', 'trocha', 'trolha', 'troucha', 'trouxa', 
    'troxa', 'tuberculoso', 'tupiniquim', 'turco', 'vaca', 'vadia', 'vagabunda', 'vagabundo', 'vagina', 'veada', 'veadao', 'veado', 'viada', 'viadao', 'víado', 'xana', 'xaninha', 'xavasca', 'xerereca', 'xexeca', 'xibiu', 'xibumba', 'xiíta', 'xochota', 'xota', 'xoxota', 'bebum', 'bêbedo', 'denigrir', 'leproso', 'mongolóide', 'índio', 'merda', 
    'porra', 'caralho', 'buceta', 'puta', 'foda-se', 'cacete', 'desgraça', 'vagabunda', 'puta', 'arrombado', 'viado', 'cu', 'pau no cu', 'viadão', 'viadinho', 'viadaopiranha', 'puta que pariu', 'puta merda', 'pqp', 'babaca', 'cuzão', 'escroto', 'fdp', 'bosta', 'fudido', 'caralha', 'corno', 'fudido', 'retardado', 'biscate', 'cachorra', 'pilantra', 'disgrama', 'puta', 'putinha', 'bicha', 'boquete', 'vagabundo', 'meretriz', 'arrombada', 'boiola', 'chupa', 'escrota', 'trouxa', 'otário', 'xota', 'xoxota', 'zorra', 'cabrona', 'puta que te pariu', 'caralho de asa', 'puta', 'cornudo', 'caralhudo', 'escrotão', 'fode', 'maldito', 'jumento', 'panaca', 'retardado', 'bct', 'caralho a quatro', 'samerda', 'saporra', 'boceta', 'bouceta', 'meretriz', 'chupa rola', 'rola', 'puta velha', 'chifrudo', 'bostinha', 'merdinha', 'cagão', 'boiolinha', 'lixo', 'merdoso', 'bundão', 'lambisgóia', 'pau mole', 'pinto', 'pintudo', 'rabo', 'safado', 'sem-vergonha', 'vagaba', 'cabaço', 'fedorento', 'peido', 'peidão', 'vagabundinho', 'rapariga', 'disgraça capeta', 'babaca', 'panaca', 'fela da puta', 'burro', 'imbecil', 'babaca', 'merda', 'escroto', 'chato', 'puta', 'cuzão', 'otário', 'pau no cu', 'desgraçado', 'vagabundo', 'lixo', 'porra', 'corno', 'foda-se', 'babaca', 'arrombado', 'bosta', 'cretino', 'fudido', 'trouxa', 'besta', 'retardado', 'nojento', 'fedido', 'inútil', 'bosta seca', 'cagão', 'fi de rapariga', 'fiderapariga', 'mocreia', 'rababaca', 'pentelho', 'merdinha', 'pau mole', 'chifrudo', 'desgraça', 'mentiroso', 'mau caráter', 'mequetrefe', 'idiota completo', 'vagaba', 'infeliz', 'paspalho', 'covarde', 'vtnc', 'canalha', 'safado', 'estúpido', 'tapado', 'macaco', 'preto', 'crioulo', 'neguinho', 'sarna preta', 'negão', 'tição', 'escurinho', 'urubu', 'mucama', 'peste negra', 'cabeça chata', 'negrada', 'pé de barro', 'favelado', 'moreno', 'pardo', 'mulato', 'daputa', 'puta', 'fdp', 'vsf', 'vaisefuder', 'sefuder', 'vaicfuder', 'tomanocu', 'tomarnocu', 'nocu', 'paunocu', 'feladaputa', 'filadaputa', 'vaosefuder', 'vãosefuder', 'm3rd@', 'm3rd4', 'p0rr4', 'p0rr@', 'vai se fuder', 'vão se fuder', 'sefude', 'arromb4do', 'sexo', 'rapariga', 'cadela', 'desgraçado', 'desgraçada', 'fodase', 'niger', 'nigger']

    lista_nao_proibida = ['Ela', 'Ele', 'Elu', 'acanalado', 'acanalador', 'acanaladura', 'acanalar', 'acanale', 'acanalhado', 'acanalhador', 'acanalhamento', 'acanalhante', 'acanalhar', 'acanalhe', 'analabo', 'analagmático', 'analampo', 'analandense', 'analcima', 'analcimo', 'analcita', 'analdia', 'analecta', 'analector', 'analectos', 'analectário', 'analema', 'analemático', 'analepse', 'analepsia', 'analfa', 'analfabetismo', 'analfabetização', 'analfabetizações', 'analfabético', 
    'analgene', 'analgesia', 'analgesina', 'analgia', 'analgésico', 'analgético', 'analisabilidade', 'analisadas', 'analisado', 'analisador', 'analisando', 'analisar', 'analise', 'analista', 'analisável', 'analiticamente', 'analitismo', 'analogamente', 'analogia', 'analogicamente', 'analogismo', 'analogista', 'analogético', 'analogístico', 'analose', 'analto', 'analuvião', 'analático', 'analéptica', 'analéptico', 'analérgico', 'analítica', 'analítico', 'analógica', 'analógico', 'analógio', 'artesanal', 'avelanal', 'baculejo', 'bacurau', 'bacuri', 'badanal', 'baiacu', 'baianal', 'banal', 'banalidade', 'banalizador', 'banalizante', 'banalizar', 'banalização', 'bananal', 'bardanal', 'barracuda', 'biscuit', 'biscuit', 'biscuit', 'bissemanal', 'brancura', 'butanal', 'cabanal', 'canal', 'canalar', 'canaleta', 'canalete', 'canalhada', 'canalhice', 'canalhismo', 'canalhocracia', 'canalhocrático', 'canaliculado', 'canaliculação', 'canaliforme', 'canalizador', 'canalizar', 'canalização', 'canalizável', 'canalículo', 'canalífero', 'cascudo', 'criptoanalisar', 'cura', 'curado', 'curador', 'curadoria', 'curanchim', 'curandeiro', 'curar', 'curarização', 'curatela', 'curatelado', 'curativo', 'curau', 'cuspe', 'cuspida', 'cuspir', 'cuspo', 'decanal', 'desanalfabetizar', 'desanalfabetização', 'desbanalizar', 'ela', 'ela', 'ele', 'elu', 'encanalhar', 'epanalepse', 'escudar', 'escudeira', 'escudeiro', 'escudela', 'escuderia', 'escudo', 'esculachado', 'esculachar', 'esculacho', 'esculhambado', 'esculhambar', 'esculhambação', 'esculpido', 'esculpir', 'escultor', 
    'escultura', 'escultural', 'escultórico', 'esculápio', 'escuma', 'escumadeira', 'escumalha', 'escumar', 'escuna', 'escupir', 'escura', 'escuras', 'escurecer', 'escuridade', 'escuridão', 'escuro', 'escusa', 'escusado', 'escusar', 'escuso', 'escusável', 'escuta', 'escutar', 'espadanal', 'especula', 'especulador', 'especular', 'especulativa', 'especulativo', 'especulação', 'espetacular', 'espetacularização', 'espetaculoso', 'espetáculo', 'fanal', 'fasciculado', 'fascículo', 'fontanal', 'germanal', 'granal', 'granalha', 'hemianalgesia', 'humanal', 'inanalisável', 'incubada', 'incubado', 'incubadora', 'incubar', 'incubação', 'inculca', 'inculcar', 'inculpado', 'inculpar', 'inculpável', 'inculto', 'inculto', 'incultura', 'inculturação', 'incumbente', 'incumbido', 'incumbir', 'incumbência', 'incumprimento', 'incunábulo', 'incursa', 'incursionar', 'incurso', 'incursão', 'incurável', 'incutir', 'infecundo', 'infecundo', 'isquianal', 'janal', 'loucura', 'macuco', 'maculado', 'macular', 'maculação', 'maculelê', 'macumba', 'macumbeiro', 'macumbeiro', 'macunaíma', 'macuru', 'macuxi', 'manalha', 'manalvo', 'metanal', 'mielanalose', 'molecular', 'molecular', 'mundanal', 'mundanalidade', 'mundanalmente', 'nanal', 'paganal', 'panal', 'pandanale', 'pantanal', 'pentáculo', 'pentáculo', 
    'pentáculo', 'perianal', 'pirarucu', 'pirarucu', 'planaltino', 'planalto', 'platanal', 'prossecução', 'prossecução', 'prossecução', 'prossecução', 'psicanalisado', 'psicanalisando', 'psicanalisar', 'psicanalismo', 'psicanalista', 'psicanalítico', 'psicoanaléptico', 'quadrissemanal', 'rabanal', 'radioanalisador', 'raquianalgesia', 'raquianalgésico', 'reanalisado', 'reanalisar', 'recanalizar', 'semanal', 'semanalmente', 'semianalfabeto', 'suburbanal', 'tanalbina', 'tercanal', 'termanalgesia', 'termanalgésico', 'timpanal', 'tocanalgesia', 'tocanalgésico', 'transversanal', 'trissemanal', 'tuberculose', 'tuberculoso', 'tuberculoso', 'uanalcuri', 'veranal']
    
    lista_proibida = set(lista_proibida) #tirando duplicatas

    comentario_split = re.split(r"\s", mensagem) # separa cada palavra na lista


    for palavra in comentario_split: #FILTRO PRINCIPAL
        palavra1 = palavra.lower() #deixa minusculo pro filtro pegar, caso não esteja no filtro a palavra não sofre alteração
        print(palavra1)
        
        if palavra1 in lista_proibida: #está na lista Proibida
            print('Na lista')
            try:
                censura = re.sub(r"\w", "*", palavra) #censura
                comentario_split[comentario_split.index(palavra)] = censura #troca o elemento a ser censurado pela censura
            except ValueError:
                print('Já filtrou')
            
        else:
            
            if re.search("[a-zA-Z]..[0-999\W]|[0-999\W]..[a-zA-z]", palavra1): #tem numero na palavra a ser censurada
                print('Tem numero ou caractere', palavra)
                val = list(palavra1)
                for c in val:
                    if c.isdigit() or c in ['@', '#', '*']:
                        index = val.index(c) # posicao do numero na palavra
                        val = ''.join(val[0:index]) # inicio ate o numero (1)
                        val1 = ''.join(val[index::]) #numero ate o final (2)
                        print(val1, val)
                        for a in lista_proibida:
                            if re.search(f"^{val}.*{val1}", a): # pesquisa se existe palavra que comeaç com (1) e termina com (2)
                                print('Filtro Numero', a)
                                try:
                                    censura = re.sub(r"\w|['@ # *']", "*", palavra) #censura
                                    comentario_split[comentario_split.index(palavra)] = censura
                                except ValueError:
                                    print('Já filtrou')
            else:
                if palavra1 in lista_nao_proibida:
                    print("lista nao proibida")
                else:
                    val = list(palavra1) #lista a palavra
                    if len(val) > 3:
                        val = val[:4] #divide mais ou menos na metade (1)
                        val2 = val[5:] #pega o final (2)
                        palavra_inic = ''.join(val)
                        palavra_final = ''.join(val2)
                        print(palavra_inic) 
                        for a in lista_proibida:
                            if re.search(fr"^{palavra_inic}.*{palavra_final}$", a): # procura palavra que comece com (1) e termine com (2)
                                print('Filtro Sem Numero', a)
                                try:
                                    censura = re.sub(r"\w", "*", palavra) #censura
                                    comentario_split[comentario_split.index(palavra)] = censura
                                    print('censura')
                                except ValueError:
                                    print('Já filtrou')
    print(comentario_split)
    return comentario_split

def comentarios(request):
    comentario_usuario = request.POST['comentario']
    codigo_materia = request.POST['materia']
    nomes = request.POST['professor'].split("$")

    # Obtenha os objetos necessários
    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_profs = []
    for n in nomes:
        obj_profs.append(Professor.objects.get(nome=n))
    obj_turma = Turma.objects.filter(materia=obj_materia)
    for prof in obj_profs:
        obj_turma = obj_turma.filter(professor=prof)
    if len(obj_turma.all())>1:
            for obj in obj_turma.all():
                if len(nomes) == len(obj.professor.all()):
                    obj_turma = obj
                    break
    else:
        obj_turma = obj_turma.get()

    user = request.user
    # print(comentario_usuario)

    comentario_split = filtro(comentario_usuario)
    
    comentario_corrigido = []

    print(comentario_split)
    for b in comentario_split: #adiciona as censuras na lista comentario_corrigido
        comentario_corrigido.append(b)
        comentario_corrigido.append(' ')

    comentario_corrigido = ''.join(comentario_corrigido) #remove da lista pro django conseguir ler
    # return comentario_corrigido

    if len(comentario_corrigido)>2 and len(comentario_corrigido)<450: #checa se o tamanho bate com as especificações
        if Comentario.objects.filter(turma=obj_turma, autor=user).exists():
            lista_numero=[]
            nova_lista=[]
            for numero in Comentario.objects.filter(turma=obj_turma, autor=user):
                numero= numero.indentificacao
                lista_numero.append(numero)
            nova_lista = sorted(lista_numero, reverse=True)
            comentario_id = int(nova_lista[0]) + 1
            novo_comentario = Comentario(autor=user, hora_publicacao=timezone.now(), turma=obj_turma, texto=comentario_corrigido, indentificacao=comentario_id) #manda o comentario pro banco de dados
            novo_comentario.save() #Fim :D
            return HttpResponse("ok")
            
        else:
            novo_comentario = Comentario(autor=user, hora_publicacao=timezone.now(), turma=obj_turma, texto=comentario_corrigido, indentificacao=1) #manda o comentario pro banco de dados
            novo_comentario.save() #Fim :D
            return HttpResponse("ok")
    else:
        return HttpResponse('nao ok')

    #a
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    print(comentario)
    print(request.method)
    if request.method == 'POST':
        print('ola mundo')
        
        texto_novo = request.POST.get('texto_novo')
        print(texto_novo, "Texto novo")
        
        filtragem = filtro(texto_novo)
        texto_novo = ' '.join(filtragem)
        
        print(texto_novo)

        if texto_novo and texto_novo != comentario.texto:
            Comentario_editado.objects.create(
                autor=comentario.autor,
                texto_antigo=comentario.texto,
                texto_novo=texto_novo,
                dia_editado=timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
    
            )
            comentario.editado = True
            comentario.texto = texto_novo
            comentario.hora_publicacao = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            comentario.save()

            return JsonResponse({'status': 'success'})

    else:
        print('entrei aqui')
        return JsonResponse({'status': 'error'})


@require_http_methods(["DELETE"])
def deletar_comentario(request, comentario_id):
    try:
        comentario = Comentario.objects.get(id=comentario_id, autor=request.user)
        comentario_text = str(comentario)
        print(comentario)
        comentario.delete()
        comentario_salvar = comentario_text.split(' ')
        print(comentario_salvar)
        txt_comentario = " ".join(comentario_salvar[9:])

    
        models_delete = Comentario_deletado(autor=comentario_salvar[7], hora=comentario_salvar[9], texto=txt_comentario, dia=comentario_salvar[5], dia_deletado= timezone.now())
        models_delete.save()
        return JsonResponse({'success': True})
        
    except Comentario.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Comentário não encontrado.'}, status=404)

def like(request):
    user = request.user
    pk_comentario = request.POST["comentario"]
    nomes = request.POST["professor"].split("$")
    
    codigo = request.POST["materia"]

    obj_materia = Materia.objects.get(codigo=codigo)
    obj_profs = []
    obj_turma = Turma.objects.filter(materia=obj_materia)
    for nome in nomes:
        obj_prof = Professor.objects.get(nome=nome)
        obj_profs.append(obj_prof)
        obj_turma = obj_turma.filter(professor=obj_prof)
    
    obj_turma = obj_turma.get()

    comentario = Comentario.objects.get(pk=pk_comentario)
    # print(obj_turma, obj_prof, comentario)
    if comentario.curtidas.filter(id=user.id).exists():
        print("vou remover o user")
        comentario.curtidas.remove(user)
    else:
        print("vou adicionar o user")
        comentario.curtidas.add(user)
    return HttpResponse(f'{comentario.curtidas.count()}')

def denuncia(request):
    user = request.user
    pk_comentario = request.POST["comentario"]
    
    nomes = request.POST["professor"].split("$")
    obj_profs = []

    codigo = request.POST["materia"]
    tipos = request.POST["pq"].split(" ")[:-1]
    traducao = {'1':True, '0':False}
    obs = request.POST["obs"] ### certo ate aqui



    obj_materia = Materia.objects.get(codigo=codigo)
    
    obj_turma = Turma.objects.filter(materia=obj_materia)

    
    for nome in nomes:
        obj_prof = Professor.objects.get(nome=nome)
        obj_profs.append(obj_prof)
        obj_turma = obj_turma.filter(professor=obj_prof)
    
    obj_turma = obj_turma.get()


    comentario = Comentario.objects.get(pk=pk_comentario)
    
    # desativar comentário se tiver mais do q 20
    print(Report.objects.filter(comentario=comentario).count())

    if Report.objects.filter(comentario=comentario).count() >= 19:
        comentario.ativo = False
        comentario.save()
        print("comentário desativado")
    
    if comentario.denuncia.filter(id=user.id).exists():
        a = 0
        return HttpResponse(f'ok')
    else:
        comentario.denuncia.add(user)
        obj_denuncia = Report(autor=user, comentario=comentario,cont_ofensivo=traducao[tipos[0]],
        info_falsa =traducao[tipos[1]],
        bullying =traducao[tipos[2]],
        cont_sexual =traducao[tipos[3]],
        discurso_odio = traducao[tipos[4]],
        observacao = obs,
        hora_publicacao = timezone.now())
        obj_denuncia.save()

        return HttpResponse(f'ok')
 



