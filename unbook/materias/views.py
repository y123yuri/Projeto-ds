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
        arg1 = 0
        # print(obj_turma.turno)
        for turno in lista_turno: #processa cada turno separado
            print(turno, 'turno inteiro')
            for i in range(len(turno)): # ler cada digito do turno
                val1 = 1
                val2 = 3
                val3 = 2
                if not turno[i].isdigit():
                    index = i  ### manha tarde ou noite, posicao onde esta a letra
                    pos = i
            if ("(" not in turno) and (")" not in turno) and ("/" not in turno) and '-' not in turno:
                
                for n in range(index): ###  pegar dia da semana
                    tamanho = len(turno[index:]) #descobrir quantas duplas pegar
                    num = len(turno[index:])//2
                    resto = len(turno[index:])%2
                    if resto != 0:
                        num +=1
                    if tamanho >= 4: #horaio diferente e dia diferente
                        for a in range(num): #vai rodar a quantia de duplas que tiver
                            try:
                                if turno[pos] == 'M': #turno Manhã
                                    dia = turno[n]+turno[pos]+turno[index+val1:index+val2]
                                    print(dia, 'dias lista M')
                                    dias.append(dia)
                                    val1 += 2
                                    val2 += 2
                            except IndexError:
                                print('error')
                                dia = turno[n]+turno[pos]+turno[len(turno)]
################################################################### divisao
                            if turno[pos] == 'T': #Turno Tarde
                                if turno[pos+1] != '1':
                                    try: # diferente de 1, metodo padrao
                                        dia = turno[n]+turno[pos]+turno[index+val1:index+val2]
                                        print(dia, 'dias lista T')
                                        dias.append(dia)
                                        val1 += 2
                                        val2 += 2
                                    except IndexError:
                                        print('error')
                                        dia = turno[n]+turno[pos] +turno[len(turno)]
                                else:
                                    try: #igual a 1, metodo diferenciado
                                        if arg1 == 0:
                                            dia = turno[n]+turno[index+0:index+2]
                                        if arg1 != 0:
                                            dia = turno[n]+turno[pos]+turno[index+1+val1:index+1+val2]
                                            arg1 += 1
                                            val1 += 2
                                            val2 += 2
                                            if dia[2] == '6': #caso exista 7T6 
                                                dia = turno[n]+'N'+'12'
                                        arg1 +=1
                                        dias.append(dia)
                                    except IndexError:
                                        print('error')
###################################################################### divisao
                            try:
                                if turno[pos] == 'N': #Turno Noite
                                    dia = turno[n]+turno[pos]+turno[index+val1:index+val2]
                                    print(dia, 'dias lista N')
                                    dias.append(dia)
                                    val1 += 2
                                    val2 += 2
                            except IndexError:
                                print('error')
                                dia = turno[n]+turno[pos]+turno[len(turno)]
                            
                    
                    else: #mesmo horario porem dias diferentes
                        dia = turno[n]+turno[index:]
                        print(dia, 'dia else')
                        dias.append(dia)
            
            else: #para estagios com filtro fodido
                print('')
        
        print(dias)
        
        #limpando a lista 
        arg2 = 0
        for f in dias: # se algo for menor que 3 na lista, remover
            try:
                if len(f) < 3:
                    dias.remove(dias[arg2])
                # limpando dois casos específicos
                if f =='7T67': 
                    dias.remove(dias[arg2]) 
                arg2 += 1
            except ValueError:
                print('')

        #conserta turnos com um numero só
        
        arg2 = 0
        for f in dias: # se tamanho = 3 e diferente de 1,5,6; remover
            try:
                if len(f) == 3: 
                    if  f[2] != '1' and f[2] != '5' and f[2] != '6': #adicionar numero subsequente
                        numero_final = int(f[2])
                        numero_final += 1
                        dias.append(f+str(numero_final))
                        dias.remove(dias[arg2])
                arg2 += 1
            except ValueError:
                print('')
                
            
        
        #conserta o caso T6
        for f in dias:
            if f[2] == '6':
                print('tem 6')
                dias.append(f[0]+'N'+'12')
        
        
        # limpando as lista DIAS denovo 
        dias = list(dict.fromkeys(dias)) # tira duplicatas
        
        arg2 = 0
        for f in dias: # se algo for menor que 3 na lista, remover
            try:
                if len(f) < 3:
                    print(len(f), 'menor que 3')
                    dias.remove(dias[arg2])
                # limpando dois casos específicos novamente
                if f =='7T67': 
                    dias.remove(dias[arg2])
                if f == '7T6':
                    dias.remove(dias[arg2]) 
                arg2 += 1
            except ValueError:
                print('')
        
        #filtro final de possibilidades de dias 
        for f in dias:
            possibilidades = ["2M12","3M12","4M12","5M12","6M12","7M12","2M34","3M34","4M34","5M34","6M34","7M34","2M5","3M5","4M5","5M5","6M5","7M5","2T1","3T1","4T1","5T1","6T1","7T1","2T23","3T23","4T23","5T23","6T23","7T23","2T45","3T45","4T45","5T45","6T45","7T45","2N12","3N12","4N12","5N12","6N12","7N12","2N34","2N34","3N34","4N34","5N34","6N34","7N34"]
            if f not in possibilidades:
                dias = possibilidades           

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
        if not Video.objects.filter(link=link).exists():
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
        if not Resumo.objects.filter(link=link).exists():
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
        if not Atividade.objects.filter(link=link).exists():
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
        
    joinha = int(separacao[3])
    
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
        if user not in obj_prof.aprovacoes.all() and lista[3]:
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

    
    lista_proibida = ['merda', 'porra', 'caralho', 'buceta', 'puta', 'foda-se', 'cacete', 'desgraça', 'vagabunda', 'filho da puta', 'arrombado', 'viado', 'cu', 'pau no cu', 'viadão' , 'viadinho' , 'viadao'
    'piranha', 'puta que pariu', 'puta merda', 'pqp', 'babaca', 'cuzão', 'escroto', 'fdp', 'bosta', 'fudido', 'caralha', 'corno', 'fudido', 'retardado', 'biscate', 'cachorra', 'pilantra' , 'disgrama', 'puta', 'putinha', ''
    'bicha', 'boquete', 'vagabundo', 'meretriz', 'arrombada', 'boiola', 'chupa', 'escrota', 'trouxa', 'otário', 'xota', 'xoxota', 'zorra', 'cabrona',
    'puta que te pariu', 'caralho de asa', 'filha da puta', 'cornudo', 'caralhudo', 'escrotão', 'filho da mãe', 'fode', 'maldito', 'jumento', 'panaca', 'retardado', 'bct', 'caralho a quatro', 'samerda', 'saporra' , ''
    'boceta', 'bouceta', 'meretriz', 'chupa rola', 'rola', 'puta velha', 'chifrudo', 'bostinha', 'merdinha', 'cagão', 'boiolinha',
    'lixo', 'merdoso', 'bundão', 'lambisgóia', 'pau mole', 'pinto', 'pintudo', 'rabo', 'safado', 'sem-vergonha', 'vagaba', 'cabaço', 'fedorento', 'peido', 'peidão', 'vagabundinho', 'rapariga', 'disgraça'
    'filho do capeta', 'babaca', 'panaca', 'fela da puta', 'burro', 'imbecil', 
    'babaca', 'merda', 'escroto', 'chato', 'filho da puta', 'cuzão', 'otário', 'pau no cu', 'desgraçado', 'vagabundo', 'lixo', 'porra', 'corno', 
    'foda-se', 'babaca', 'arrombado', 'bosta', 'cretino', 'fudido', 'trouxa', 'besta', 'retardado', 'nojento', 'fedido', 'inútil', 'bosta seca', 'cagão', 'fi de rapariga', 'fiderapariga' , 'mocreia' , 'ra'
    'babaca', 'pentelho', 'merdinha','pau mole', 'chifrudo', 'desgraça', 
    'mentiroso', 'mau caráter', 'mequetrefe', 'idiota completo', 'vagaba', 'infeliz', 'paspalho', 'covarde', 'vtnc',
    'canalha', 'safado', 'estúpido', 'tapado','macaco', 'preto', 'crioulo', 'neguinho', 'sarna preta', 'negão', 'tição', 
    'escurinho', 'urubu', 'mucama', 'peste negra', 'cabeça chata', 'negrada', 'pé de barro', 'favelado', 'moreno', 'pardo', 'mulato',
    'daputa', 'filhadaputa', 'fdp', 'vsf', 'vaisefuder', 'sefuder', 'vaicfuder', 'tomanocu', 'tomarnocu', 'nocu', 'paunocu', 'feladaputa', 'filadaputa', 'vaosefuder', 'vãosefuder', 'm3rd@', 'm3rd4', 'p0rr4', 'p0rr@', 
    'vai se fuder', 'vão se fuder', 'sefude', 'arromb4do', 'sexo', 'rapariga', 'cadela' , 'desgraçado', 'desgraçada', 'fodase']

    comentario_split = comentario_usuario.split(' ')
    # print(comentario_split)
    novo_if_comentario = []
    for palavra in comentario_split: #pega todas as palavras
        palavra_minuscula = palavra.lower()
        if palavra_minuscula in lista_proibida:
            contador = 0
            for letra in palavra_minuscula:
                contador += 1
            palavra = contador * '*'
        novo_if_comentario.append(palavra)
         
    ########################################## 
    comentario_corrigido = ''
    for palavra2 in novo_if_comentario:
        comentario_corrigido += f'{palavra2} ' 

   
    if len(comentario_corrigido)>2:
        novo_comentario = Comentario(autor=user, hora_publicacao=timezone.now(), turma=obj_turma, texto=comentario_corrigido)
        novo_comentario.save()
        return HttpResponse("ok")
    else:
        return HttpResponse("nao ok")
    
    


@require_http_methods(["DELETE"])
def deletar_comentario(request, comentario_id):
    try:
        comentario = Comentario.objects.get(id=comentario_id, autor=request.user)
        comentario_text = str(comentario)
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
 



