from django.shortcuts import render, redirect
from .forms import CadastroForm
from .forms import LoginForm
from .forms import Esqueceu_senhaForm
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Cadastro
from .models import Username_trocado
from .models import Senha_trocada
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from .models import PasswordResetToken
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import Nova_senhaForm
from django.contrib import messages
from .utils import send_activation_email
from .forms import PerfilForm
from .models import PerfilUsuario
from .models import Cursos_unb
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from datetime import timezone
import json
from django.utils.timezone import make_aware
from django.utils import timezone
# Create your views here.

def cadastro(request):
    context = {}
    form = CadastroForm()
    context["form"] = form
    return render(request, "html/cadastro.html", context)

def verificar(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True #ativa o usuário
        user.save() #salva o usuario e nao loga
        messages.success(request, 'Sua conta foi ativada com sucesso!')
        return redirect('/cadastro/verificar/ativado')
    else:
        messages.error(request, 'Link de ativação inválido!')
        return redirect('/')

def ativado(request):
    return render(request, 'html/Ativado.html')

def sucesso(request):
    if request.method == 'POST':
        obj = User()
        f = CadastroForm(request.POST, instance=obj)
        context = {}
        
        if 'erro' in request.session:
            del request.session['erro']
        
        if f.is_valid():
            print(type(f), f.cleaned_data, type(obj))
            context["resposta"] = f.cleaned_data
            print(context)
            dados = context['resposta']
            name_variavel = dados['name']
            nome_variavel = dados['username']
            email_variavel = dados['email'] 
            senha_variavel = dados['password']
            senha_confirma_variavel = dados['senha_confirma']
            try:
                email_numero = int(email_variavel[:9])
            except:
                email_numero = str(email_variavel[:9])
            print(email_numero, type(email_numero))
            dados = [nome_variavel, email_variavel, senha_variavel, name_variavel]
            if dados[1][dados[1].index('@'):] == "@aluno.unb.br" and len(dados[0]) <= 12  and type(email_numero)==int and len(email_variavel) == 22 :
                if User.objects.filter(email=dados[1]).exists() or User.objects.filter(username=dados[0]).exists():
                    messages.error(request, 'O email ou usuário já existe!!') 
                    print('Ja existe email')
                    return JsonResponse({'success': False, 'error': 'O email ou usuário já existe!!'})
                
                else:
                    if senha_variavel != senha_confirma_variavel:
                        return JsonResponse({'success': False, 'error': 'Senhas não coincidem!!'})
                    else:
                        user = User.objects.create_user(username=dados[0], email=dados[1], password=dados[2], first_name=dados[3])
                        print("User Criado")
                        user.is_active = False 
                        user.save()
                        send_activation_email(user, request)
                        print("Enviou email de ativação")
                        return JsonResponse({'success': True, 'username': user.username})
                
                
            else:
                messages.error(request, 'Erro no cadastro!!') 

                request.session['erro'] = "Já existe um cadastro com o email ou nome de usuario"
                return JsonResponse({'success': False, 'error': 'Formulário inválido, Erro 707'})
            
        else:
            request.session['erro'] = "Já existe um cadastro com o email ou nome de usuario"
            return JsonResponse({'success': False, 'error': 'Erro no cadastro, alguns requisitos não foram devidamente enviados!!'})
    
    return render(request, "html/VerificaEmail.html")

def nao_recebi(request): #Nao recebi o email de ativacao 
    context = {}
    form = Esqueceu_senhaForm()
    context["form"] = form
    return render(request, "html/recebiEmailNN.html", context)

def envio_novo(request): #envia o email de ativacao pra quem nao recebeu o email de ativacao
    if request.method == 'POST':
        context = {}
        f = Esqueceu_senhaForm(request.POST)
        if f.is_valid():
            context["resposta"] = f.cleaned_data
            print(context['resposta'])
            email = context["resposta"]["email"]
            usuario = User.objects.filter(email=email)
            if usuario:
                usuario = usuario[0]
                if User.objects.filter(email=email).exists() and not usuario.is_active:
                    send_activation_email(usuario, request)
                    return redirect('../../') # cadastro/sucesso
                else:
                    request.session['erro'] = "usuario já esta ativo"
                    return redirect('/cadastro/login', request) #retorna para a aba de login em caso de email já ativado (usuario ja ativado)
            else:
                request.session['erro'] = "usuario não existe"
                return redirect('../../../', request) #retorna para a aba de cadastro em caso de email nao existente (usuario nao existe)
            
        return JsonResponse({'success': False, 'error': 'Erro no sistema, 909!!'})
    else:           
        return JsonResponse({'success': False, 'error': 'isso não vai acontecer!!'})

    
def login_func(request):
    if not request.user.is_authenticated:
        context = {}
        form = LoginForm()
        context["form"] = form
        
        return render(request, "html/Login.html", context)
    elif request.user.is_authenticated or request.user.is_active:
        context = {}
        form = PerfilForm()
        context["form"] = form
        user= request.user
        try:
            perfil_existente = PerfilUsuario.objects.filter(user=user).first()
        except PerfilUsuario.DoesNotExist:
            pass  # Ou alguma lógica alternativa caso o perfil não exista
    
        context = {
            'perfil': perfil_existente
        }

        return render(request, "html/Perfil.html", context) 
    



def logado(request):
    f = LoginForm(request.POST)
    context = {}
    if 'erro' in request.session:
        del request.session['erro']
    if f.is_valid():
        context["resposta"] = f.cleaned_data
        email_variavel = f.cleaned_data["email"]
        senha_variavel = f.cleaned_data["password"]
        dados = [email_variavel, senha_variavel] #tratamento de dados
        # print(User.objects.get(email=f'{email_variavel}'))
        
        try:
            user = User.objects.get(email=f'{email_variavel}')
            if not user.is_active:
                print("nao está ativo")
                return render(request, "html/VerificaEmail.html")
            v1 = user.username
            user = authenticate(username=f'{v1}', password=f'{senha_variavel}')
            print(v1)
            if user:  
                login(request, user)
                return redirect('login_func')
            else:
                request.session['erro'] = "Login invalido"
        
    
            return redirect("../")
        except User.DoesNotExist:
            print("Usuário não existe")
            request.session['erro'] = "Login invalido, usuário não existe"
            return redirect("../")

    
def logout(request):
    auth.logout(request)
    return redirect('login_func')

def usuario(request):
    context = {}

    if request.method == 'POST':
        # Pesquisa de cursos
        if 'input_cursos' in request.POST:
            termo_pesquisa = request.POST['input_cursos']
            obj_lista = Cursos_unb.objects.filter(curso__icontains=termo_pesquisa)
            
            resposta = ''
            if len(obj_lista) > 0:
                resposta = obj_lista[0].curso + ','
                if len(obj_lista) > 1:
                    for obj in obj_lista[1:]:
                        resposta += ";" + obj.curso
            
            return HttpResponse(resposta)
        if request.method == 'POST':
            curso = request.POST.get('curso')
            semestre = request.POST.get('semestre')
            bio = request.POST.get('bio')
            visibilidade = request.POST.get('visibilidade')
            foto =  request.POST.get('foto')

            
            print('print localizacao')
            perfil = PerfilUsuario.objects.get(user=request.user)
            if curso:
                perfil.curso = curso
                print(perfil.curso)
            if semestre and semestre != "Semestre":
                perfil.semestre = semestre
                print(perfil.semestre)
            if bio:
                perfil.descricao = bio
                print(perfil.descricao)
            if visibilidade:
                
                if visibilidade == '0':
                    print('entrei nessa merda')
                    print(visibilidade)
                    perfil.privacidade = False
                else:
                    perfil.privacidade = True
                    print('entrei nessa merda 2 ')
                    print(visibilidade)
            if foto:
                print(foto)
                perfil.foto = int(foto)
                print(perfil.foto, 'perfil foto')
                    
            
            perfil.save()
            return redirect('../', context) , JsonResponse({'status':'sucess'})
        return JsonResponse({'status': 'fail'}, status=400)

def trocar_senha(request):
    if request.method == 'POST':
        senha_antiga = request.POST.get('senha_antiga')
        senha_nova = request.POST.get('senha_nova')
        senha_nova_confirma = request.POST.get('senha_nova_confirma')
        if not request.user.check_password(senha_antiga):
            messages.error(request, 'Senha antiga incorreta.')
            return redirect('login_func')
        if senha_nova != senha_nova_confirma:
            messages.error(request, 'As novas senhas não coincidem.')
            return redirect('login_func')
        request.user.set_password(senha_nova)
        request.user.save()
        Senha_trocada.objects.create(
                            user=user,
                            data_troca=timezone.now()  
                        )
        update_session_auth_hash(request, request.user)  
        messages.success(request, 'Senha alterada com sucesso!')
        return redirect('login_func')  


def esqueceu(request):
    context = {}
    form = Esqueceu_senhaForm()
    context["form"] = form
    return render (request, "html/Nova_senha_email.html", context)

def email_recupera(request):
    
    f = Esqueceu_senhaForm(request.POST)
    context = {}
    
    if 'erro' in request.session:
        del request.session['erro']
    if f.is_valid():
        context["resposta"] = f.cleaned_data
        email_variavel = f.cleaned_data["email"]
        
        try:
            user = User.objects.get(email=email_variavel)
        except User.DoesNotExist:
            request.session['erro'] = "Email não encontrado"
            return render(request, 'html/Nova_senha_email.html') #nova senha de botar o email para recuperar
        token = PasswordResetToken.objects.create(user=user)

        reset_url = request.build_absolute_uri(
            reverse('novaSenha', kwargs={'token': str(token.token)})
        )

        subject = "Redefinição de senha"
        message = render_to_string('html/redefinição.html', {
            'user': user,
            'reset_url': reset_url
        })
        send_mail(subject, message, 'django.core.mail.backends.smtp.EmailBackend', [reset_url] ,[user.email])

        return render(request, 'html/Nova_senha_confirma.html', context)

    else:
        request.session['erro'] = "Email invalido"
        return redirect("./")
    
def novaSenha(request, token):
    context = {}
    token_obj = get_object_or_404(PasswordResetToken, token=token)
    
    f = Nova_senhaForm(request.POST)
    context = {}

    # Verifica se o token é válido
    if not token_obj.is_valid():
        context["erro"] = "Token inválido ou expirado"
        return render(request, "html/Nova_senha_email.html", context)
        
    # Se o método da requisição for POST, processa o formulário
    if token_obj.is_valid():
        form = Nova_senhaForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get("password")
            token_obj.user.set_password(new_password)
            token_obj.user.save()
            return redirect("login_func")
        else:
            
            context["erro"] = "Erro ao processar o formulário. Por favor, tente novamente."
    
    # Se o método da requisição for GET, exibe o formulário
    else:
        form = Nova_senhaForm()
        
    
    context["form"] = form
    return render(request, "html/Nova_senha.html", context)


def username(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_username = data.get('username')
        print(new_username)
        new_username=new_username.strip()
        print(new_username)
        if new_username and request.user.is_authenticated:
            if User.objects.filter(username=new_username).exists(): ### verifica se ja existe
                return JsonResponse({'success': False, 'error': 'Usuario já existente, escolha outro!'})
            else:
                if 2< len(new_username) <12:
                    for i in new_username:
                        if i == '.':
                            return JsonResponse({'status': 'error', 'message': 'Usuario não pode conter ponto "."'}, status=400)
                            break
                        elif i == ' ':
                            return JsonResponse({'status': 'error', 'message': 'Usuario não pode conter espaço '}, status=400)
                        else:
                            pass
                    user = request.user # descobrir o nome dele
                    username_antigo = user #salvar a trroca no banco de dados
                    user.username = new_username #novo username
                    user.save()
                    Username_trocado.objects.create(
                            user=user,
                            username_antigo=username_antigo,
                            novo_username=new_username,
                            data_troca=timezone.now()  
                        )
                    return JsonResponse({'status': 'success'}, status=200)
                else:
                    return JsonResponse({'status': 'error', 'message': 'Usuario menor que 3 caracteres ou maior que 12! '}, status=400)
        return JsonResponse({'status': 'error', 'message': 'Falha ao trocar o username'}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Erro no formulário'}, status=405)





