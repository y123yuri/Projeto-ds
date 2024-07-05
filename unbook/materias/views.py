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

# Create your views here.

def home(request):
    user= request.user
    if request.user.is_authenticated:
        perfil_existente = PerfilUsuario.objects.filter(user=user).first()
        context = {
            'perfil': perfil_existente
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


def materia(request, codigo, nome):
    if request.user.is_authenticated:
        # print(codigo, nome)
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
        context["quant_like"] = []
        context["curtidas"] = []
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
                    contador_true+=1
                    lista_curtidas.append(True)
                else:
                    contador_true+=1
                    lista_curtidas.append(False)
    
        for c in lista_curtidas:
            if c == True:
                lista_fodase.append(1)
            else:
                lista_fodase.append(0)
        lista_fodase.sort(reverse=True)
        for c in lista_fodase:
            if c == 1:
                context["curtidas"].append(True)
            if c == 0:
                 context["curtidas"].append(False)

        # print(context['curtidas'])
        
        
        
        for c in range(0,len(pre_context_curtida)):
            nova = [pre_context[c]],[pre_context_curtida[c]]
            lista_tudao.append(nova)
        
        nova_lista = sorted(lista_tudao, key=lambda lista_tudao:lista_tudao[1], reverse=True) 
        


        

        for c in nova_lista:
            comentarios_nova_lista=c[0]
            curtidas_nova_lista=c[1]
            
            context_comentario_final.append(comentarios_nova_lista)
            context_curtida_final.append(curtidas_nova_lista)
        
        for d in context_comentario_final:
            x= d[0]
            context["comentarios"].append(x)

        for e in context_curtida_final:
            x= e[0]
            context["quant_like"].append(x)
            
        


        

        
        
        index =0
        lista_turno = obj_turma.turno.split(" ")
        dias = []
        
        # print(obj_turma.turno)
        for turno in lista_turno: #processa cada turno separado
            print(turno, 'turno inteiro')
            #tamanho do turno
            for i in range(len(turno)): # ler cada digito do turno
                if not turno[i].isdigit():
                    index = i  ### manha tarde ou noite, posicao onde esta a letra
                    print(index, 'index')
                    arg = index + 1
                    print(arg, 'arg')
            if ("(" not in turno) and (")" not in turno) and ("/" not in turno) and '-' not in turno:
#
                for n in range(index): ###  pegar dia da semana
                    arg = index + 1
                    print(n, 'passou')
                    tamanho = len(turno)
                    print(tamanho, 'tamanho')
                    if tamanho >= 4: #horaio diferente e dia diferent
                        for i in range(len(turno[index:])+1):
                            try:
                                dia = turno[n]+turno[index]+turno[arg]
                                arg += 1
                                print(dia, 'dia if', i)
                                dias.append(dia)
                            except IndexError:
                                print('IndexError')
                                
                    else: #mesmo horario porem dias diferentes
                        dia = turno[n]+turno[index:]
                        print(dia, 'dia else')
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

def add_video(request): #ajax function
    materia = Materia.objects.get(codigo=request.POST["materia"])
    professor = Professor.objects.get(nome=request.POST["professor"])
    turma = Turma.objects.get(materia=materia, professor=professor)
    nome_link = request.POST["titulo"]
    link = request.POST["link"].replace("https://", "").replace("www.", "")
    
    print(f"link: {link}; nome:{nome_link} video")
    if link[:11] == "youtube.com" or link[:16] == "drive.google.com":
        #filtro de videos
        if not Video.objects.filter(link=link,turma=turma).exists() :
            print("oi")
            video = Video(
                turma=turma,
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
    
    




def resumos(request, nome,codigo) :
    if request.user.is_authenticated:
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_prof = Professor.objects.get(nome=nome)

        obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
        context = {}
        context["turma"] = obj_turma
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

def add_resumo(request): #ajax function
    materia = Materia.objects.get(codigo=request.POST["materia"])
    professor = Professor.objects.get(nome=request.POST["professor"])
    turma = Turma.objects.get(materia=materia, professor=professor)
    nome_link = request.POST["titulo"]
    link = request.POST["link"].replace("https://", "").replace("www.", "")
    
    print(f"link: {link}; nome:{nome_link} resumo")
    if link[:11] == "youtube.com" or link[:16] == "drive.google.com" or link[:15] =='docs.google.com' or link[:19] == 'teams.microsoft.com':
        #filtro de resumo
        if not Resumo.objects.filter(link=link, turma=turma).exists():
            print("oi")
            resumo = Resumo(
                turma=turma,
                hora_publicacao=timezone.now(),
                titulo=nome_link,
                link=link,
                autor=request.user)
            resumo.save()
            return HttpResponse("ok")
        else:
            messages.error(request, 'O link postado já existe ou é inválido.')
            return HttpResponse("ok")
        return HttpResponse("erro")
    else:
        return HttpResponse("erro")




def atividades(request, nome,codigo) :
    if request.user.is_authenticated:
        obj_materia = Materia.objects.get(codigo=codigo)
        obj_prof = Professor.objects.get(nome=nome)

        obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
        context = {}
        context["turma"] = obj_turma
        lista_atividades = []
        lista_quant_curtida = []
        lista_bool_curtiu = []
        for atividade in Atividade.objects.filter(turma=obj_turma):
            lista_atividades.append(atividade)
            lista_quant_curtida.append(atividade.curtidas.count())
            lista_bool_curtiu.append( 1 if atividade.curtidas.filter(id=request.user.id).exists() else 0)

        # dps implementar ordenação em uma FUNÇÃO

        context["atividades"] = lista_atividades
        context["bool_curtiu"] = lista_bool_curtiu
        context["quant_curtidas"] = lista_quant_curtida

        return render(request, "Atividades.html", context)
    else:
        context = {}
        context["erro"] = "Você precisa estar logado" 
        return redirect('../../cadastro/login', context)


def add_atividade(request):
    materia = Materia.objects.get(codigo=request.POST["materia"])
    professor = Professor.objects.get(nome=request.POST["professor"])
    turma = Turma.objects.get(materia=materia, professor=professor)
    nome_link = request.POST["titulo"]
    link = request.POST["link"].replace("https://", "").replace("www.", "")
    context = {}
    print(f"link: {link}; nome:{nome_link} atividade")
    if link[:11] == "youtube.com" or link[:16] == "drive.google.com":
        #filtro de atividade
        if not Atividade.objects.filter(link=link,turma=turma).exists():
            print("oi")
            atividade = Atividade(
                turma=turma,
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
    nome_prof = request.POST['professor']

    # Obtenha os objetos necessários
    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_prof = Professor.objects.get(nome=nome_prof)
    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)

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
        if user in obj_prof.aprovacoes.all():
            if joinha == 0 :
                obj_prof.aprovacoes.remove(user)
            else:
                if user not in obj_prof.aprovacoes:
                    obj_prof.aprovacoes.add(user)
    else:
        # O usuário não avaliou, então adicionamos a avaliação e incrementamos o contador
        numero_avaliacoes += 1

        # Calcule as novas médias incluindo a nova avaliação
        nova_dificuldade = ((obj_turma.avaliacao_dificuldade * (numero_avaliacoes - 1)) + dificuldade_dados) // numero_avaliacoes
        nova_apoio = ((obj_turma.avaliacao_apoio_aluno * (numero_avaliacoes - 1)) + apoio_dados) // numero_avaliacoes
        nova_didatica = ((obj_turma.avaliacao_didatica * (numero_avaliacoes - 1)) + didatica_dados) // numero_avaliacoes
        if user not in obj_prof.aprovacoes.all():
            if joinha == 1 :
                obj_prof.aprovacoes.add(user)


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
    


def comentarios(request):
    comentario_usuario = request.POST['comentario']
    codigo_materia = request.POST['materia']
    nome_prof = request.POST['professor']

    # Obtenha os objetos necessários
    obj_materia = Materia.objects.get(codigo=codigo_materia)
    obj_prof = Professor.objects.get(nome=nome_prof)
    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)

    user = request.user
    # print(comentario_usuario)
    ##################################

####################################### Arrumei Saporra
    import re

    lista_proibida = ['merda', 'porra', 'caralho', 'buceta', 'puta', 'foda se', 'cacete', 'desgraça', 'vagabunda', 'puta', 'arrombada', 'viado', 'cu', 'pau no cu', 'piranha', 'puta que pariu', 'puta merda', 'pqp', 'babaca', 'cuzão', 'escroto', 'fdp', 'bosta', 'fudido', 'caralha', 'corno', 'fudido', 'retardado', 'biscate', 'bicha', 'boquete', 'vagabundo', 'meretriz', 'arrombada', 'boiola', 'cabrão', 'chupa', 'escrota', 'trouxa', 'otário', 'xota', 'xoxota', 'zorra', 'cabrona', 'puta que te pariu', 'caralho de asa', 'puta', 'cornudo', 'caralhudo', 'escrotão', 'fode', 'maldito', 'jumento', 'panaca', 'retardado', 'paspalho', 'mané', 'boceta', 'trouxa', 'besta', 'ralé', 'meretriz', 'chupa rola', 'rola', 'puta velha', 'chifrudo', 'bostinha', 'merdinha', 'cagão', 'boiolinha', 'lixo', 'merdoso', 'bundão', 'lambisgóia', 'fedido', 'pau mole', 'pinto', 'pintudo', 'rabo', 'rabo de saia', 'safado', 'sem-vergonha', 'vagaba', 'bobo da corte', 'espermatozóide', 'cuspidor', 'coxinha', 'cabaço', 'fedorento', 'peido', 'peidão', 'vagabundinho', 'esquema', 'casca de ferida', 'bagulho', 'mentecapto', 'caga-regra', 'saco', 'saco cheio', 'capeta', 'inferno', 'tornozelo', 'babaca', 'panaca', 'fela da puta', 'fuder', 'velha', 'foder', 'sexo', 'fds', 'africano', 'aleijado', 'analfabeto', 'anus', 'anão', 'apenado', 'baba-ovo', 'babaca', 'babaovo', 'bacura', 'bagos', 'baianada', 'baitola', 'barbeiro', 'barraco', 'beata', 'bebum', 'besta', 'bicha', 'bisca', 'bixa', 'boazuda', 'boceta', 'boco', 'boiola', 'bolagato', 'bolcat', 'boquete', 'bosseta', 'bosta', 'bostana', 'branquelo', 'brecha', 'brexa', 'brioco', 'bronha', 'buca', 'buceta', 'bugre', 'bunda', 'bunduda', 'burra', 'burro', 'busseta', 'bárbaro', 'bêbado', 'cachorra', 'cachorro', 'cadela', 'caga', 'cagado', 'cagao', 'cagona', 'caipira', 'canalha', 'canceroso', 'caralho', 'casseta', 'cassete', 'ceguinho', 'checheca', 'chereca', 'chibumba', 'chibumbo', 'chifruda', 'chifrudo', 'chochota', 'chota', 'chupada', 'chupado', 'ciganos', 'clitoris', 'cocaina', 'coco', 
    'comunista', 'corna', 'corno', 'cornuda', 'cornudo', 'corrupta', 'corrupto', 'coxo', 'cretina', 'cretino', 'crioulo', 'cruz-credo', 'cu', 'culhao', 'curalho', 'cuzao', 'cuzuda', 'cuzudo', 'debil', 'debiloide', 'deficiente', 'defunto', 'demonio', 'denegrir', 'detento', 'difunto', 'doida', 'doido', 'egua', 'elemento', 'encostado', 'esclerosado', 'escrota', 'escroto', 'esporrada', 'esporrado', 'esporro', 'estupida', 'estupidez', 'estupido', 'fanático', 'fascista', 'fedida', 'fedido', 'fedor', 'fedorenta', 'feia', 'feio', 'feiosa', 'feioso', 'feioza', 'feiozo', 'felacao', 'fenda', 'fode', 'fodida', 'fodido', 'fornica', 'fornição', 'fudendo', 'fudeção', 'fudida', 'fudido', 'furada', 'furado', 'furnica', 'furnicar', 'furo', 'furona', 'furão', 'gaiata', 'gaiato', 'gay', 'gilete', 'goianada', 'gonorrea', 'gonorreia', 'gosmenta', 
    'gosmento', 'grelinho', 'grelo', 'gringo', 'homo-sexual', 'homossexual', 'homossexualismo', 'idiota', 'idiotice', 'imbecil', 'inculto', 'iscrota', 'iscroto', 'japa', 'judiar', 'ladra', 'ladrao', 'ladroeira', 'ladrona', 'ladrão', 'lalau', 'lazarento', 'leprosa', 'leproso', 'louco', 'lésbica', 'macaca', 'macaco', 'machona', 'macumbeiro', 'malandro', 'maluco', 'maneta', 'marginal', 'masturba', 'meleca', 'meliante', 'merda', 'mija', 'mijada', 'mijado', 'mijo', 'minorias', 'mocrea', 'mocreia', 'moleca', 'moleque', 'mondronga', 'mondrongo', 'mongol', 'mulato', 'naba', 'nadega', 'nazista', 'negro', 'nojeira', 'nojenta', 'nojento', 'nojo', 'olhota', 'otaria', 'otario', 'otária', 
    'otário', 'paca', 'palhaço', 'paspalha', 'paspalhao', 'paspalho', 'pau', 'peia', 'peido', 'pemba', 'pentelha', 'pentelho', 'perereca', 'perneta', 'peru', 'peão', 'pica', 
    'picao', 'pilantra', 'pinel', 'piranha', 'piroca', 'piroco', 'piru', 'pivete', 'político', 'porra', 'prega', 'preso', 'prost-bulo', 'prostibulo', 'prostituta', 'prostituto', 'punheta', 'punhetao', 'pus', 'pustula', 'puta', 'puto', 'puxa-saco', 'puxasaco', 'pênis', 'rabao', 'rabo', 'rabuda', 'rabudao', 'rabudo', 'rabudona', 'racha', 'rachada', 'rachadao', 'rachadinha', 'rachadinho', 'rachado', 'ramela', 'remela', 'retardada', 'retardado', 'roceiro', 'rola', 'rolinha', 'rosca', 'sacana', 'safada', 'safado', 'sapatao', 'sapatão', 'sifilis', 'siririca', 'tarada', 'tarado', 'tesuda', 'tezao', 'tezuda', 'tezudo', 'traveco', 'trocha', 'trolha', 'troucha', 'trouxa', 
    'troxa', 'tuberculoso', 'tupiniquim', 'turco', 'vaca', 'vadia', 'vagabunda', 'vagabundo', 'vagina', 'veada', 'veadao', 'veado', 'viada', 'viadao', 'víado', 'xana', 'xaninha', 'xavasca', 'xerereca', 'xexeca', 'xibiu', 'xibumba', 'xiíta', 'xochota', 'xota', 'xoxota', 'bebum', 'bêbedo', 'denigrir', 'leproso', 'mongolóide', 'índio', 'merda', 
    'porra', 'caralho', 'buceta', 'puta', 'foda-se', 'cacete', 'desgraça', 'vagabunda', 'puta', 'arrombado', 'viado', 'cu', 'pau no cu', 'viadão', 'viadinho', 'viadaopiranha', 'puta que pariu', 'puta merda', 'pqp', 'babaca', 'cuzão', 'escroto', 'fdp', 'bosta', 'fudido', 'caralha', 'corno', 'fudido', 'retardado', 'biscate', 'cachorra', 'pilantra', 'disgrama', 'puta', 'putinha', 'bicha', 'boquete', 'vagabundo', 'meretriz', 'arrombada', 'boiola', 'chupa', 'escrota', 'trouxa', 'otário', 'xota', 'xoxota', 'zorra', 'cabrona', 'puta que te pariu', 'caralho de asa', 'puta', 'cornudo', 'caralhudo', 'escrotão', 'fode', 'maldito', 'jumento', 'panaca', 'retardado', 'bct', 'caralho a quatro', 'samerda', 'saporra', 'boceta', 'bouceta', 'meretriz', 'chupa rola', 'rola', 'puta velha', 'chifrudo', 'bostinha', 'merdinha', 'cagão', 'boiolinha', 'lixo', 'merdoso', 'bundão', 'lambisgóia', 'pau mole', 'pinto', 'pintudo', 'rabo', 'safado', 'sem-vergonha', 'vagaba', 'cabaço', 'fedorento', 'peido', 'peidão', 'vagabundinho', 'rapariga', 'disgraça capeta', 'babaca', 'panaca', 'fela da puta', 'burro', 'imbecil', 'babaca', 'merda', 'escroto', 'chato', 'puta', 'cuzão', 'otário', 'pau no cu', 'desgraçado', 'vagabundo', 'lixo', 'porra', 'corno', 'foda-se', 'babaca', 'arrombado', 'bosta', 'cretino', 'fudido', 'trouxa', 'besta', 'retardado', 'nojento', 'fedido', 'inútil', 'bosta seca', 'cagão', 'fi de rapariga', 'fiderapariga', 'mocreia', 'rababaca', 'pentelho', 'merdinha', 'pau mole', 'chifrudo', 'desgraça', 'mentiroso', 'mau caráter', 'mequetrefe', 'idiota completo', 'vagaba', 'infeliz', 'paspalho', 'covarde', 'vtnc', 'canalha', 'safado', 'estúpido', 'tapado', 'macaco', 'preto', 'crioulo', 'neguinho', 'sarna preta', 'negão', 'tição', 'escurinho', 'urubu', 'mucama', 'peste negra', 'cabeça chata', 'negrada', 'pé de barro', 'favelado', 'moreno', 'pardo', 'mulato', 'daputa', 'puta', 'fdp', 'vsf', 'vaisefuder', 'sefuder', 'vaicfuder', 'tomanocu', 'tomarnocu', 'nocu', 'paunocu', 'feladaputa', 'filadaputa', 'vaosefuder', 'vãosefuder', 'm3rd@', 'm3rd4', 'p0rr4', 'p0rr@', 'vai se fuder', 'vão se fuder', 'sefude', 'arromb4do', 'sexo', 'rapariga', 'cadela', 'desgraçado', 'desgraçada', 'fodase']

    lista_proibida = set(lista_proibida) #tirando duplicatas
    comentario_corrigido = []

    comentario_split = re.split(r"\s", comentario_usuario) # separa cada palavra na lista


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
            if re.search("[0-9]", palavra): #tem numero na palavra a ser censurada
                print('Tem numero ou caractere', palavra)
                val = list(palavra1)
                for c in val:
                    if c.isdigit():
                        index = val.index(c) # posicao do numero na palavra
                        val = ''.join(val[0:index]) # inicio ate o numero (1)
                        val1 = ''.join(val[index::]) #numero ate o final (2)
                        for a in lista_proibida:
                            if re.search(f"^{val}.*{val1}", a): # pesquisa se existe palavra que comeaç com (1) e termina com (2)
                                print('Filtro Numero', a)
                                try:
                                    censura = re.sub(r"\w", "*", palavra) #censura
                                    comentario_split[comentario_split.index(palavra)] = censura
                                except ValueError:
                                    print('Já filtrou')
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
    for b in comentario_split: #adiciona as censuras na lista comentario_corrigido
        comentario_corrigido.append(b)
        comentario_corrigido.append(' ')

    comentario_corrigido = ''.join(comentario_corrigido) #remove da lista pro django conseguir ler

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

    if request.method == 'POST':
        texto_novo = request.POST.get('texto_novo')
        if texto_novo and texto_novo != comentario.texto:
            Comentario_editado.objects.create(
                autor=comentario.autor,
                texto_antigo=comentario.texto,
                texto_novo=texto_novo,
                dia_editado=timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
                indentificacao=comentario.id
            )
            comentario.texto = texto_novo
            comentario.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


@require_http_methods(["DELETE"])
def deletar_comentario(request, comentario_id):
    try:
        comentario = Comentario.objects.get(id=comentario_id, autor=request.user)
        comentario_text = str(comentario)
        print(comentario)
        comentario.delete()
        comentario_salvar = comentario_text.split(' ')
        models_delete = Comentario_deletado(autor=comentario_salvar[4], hora=comentario_salvar[3], texto=comentario_salvar[6], dia=comentario_salvar[2], dia_deletado= timezone.now())
        models_delete.save()
        return JsonResponse({'success': True})
        
    except Comentario.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Comentário não encontrado.'}, status=404)

def like(request):
    user = request.user
    pk_comentario = request.POST["comentario"]
    nome = request.POST["professor"]
    codigo = request.POST["materia"]

    obj_materia = Materia.objects.get(codigo=codigo)
    obj_prof = Professor.objects.get(nome=nome)
    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
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
    nome = request.POST["professor"]
    codigo = request.POST["materia"]
    tipos = request.POST["pq"].split(" ")[:-1]
    traducao = {'1':True, '0':False}
    obs = request.POST["obs"]

    obj_materia = Materia.objects.get(codigo=codigo)
    obj_prof = Professor.objects.get(nome=nome)
    obj_turma = Turma.objects.get(materia=obj_materia, professor=obj_prof)
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
 



