from django.shortcuts import render, redirect
from .forms import CadastroForm
from .forms import LoginForm
from .forms import Esqueceu_senhaForm
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Cadastro
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
        user.is_active = True
        user.save()
        login(request, user)
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
            #print(context)
            dados = context['resposta']
            nome_variavel = dados['username']
            email_variavel = dados['email']
            senha_variavel = dados['password']
            dados = [nome_variavel, email_variavel, senha_variavel]
            if dados[1][dados[1].index('@'):] == "@aluno.unb.br":
                user = User.objects.create_user(username=dados[0], email=dados[1], password=dados[2])
                user.is_active = False 
                user.save()
                send_activation_email(user, request)
                return JsonResponse({'success': True, 'username': user.username}) 
            else:
                request.session['erro'] = "já existe um cadastro com o email ou nome de usuario"
                return JsonResponse({'success': False, 'error': 'Formulário inválido'})
            
        else:
            request.session['erro'] = "já existe um cadastro com o email ou nome de usuario"
            return JsonResponse({'success': False, 'error': 'Formulário inválido'})
    
    return render(request, "html/VerificaEmail.html")


def login_func(request):
    if not request.user.is_authenticated:
        context = {}
        form = LoginForm()
        context["form"] = form
        
        return render(request, "html/Login.html", context)
    elif request.user.is_authenticated:
        return render(request,"html/Perfil.html") # trocar depois pra página de perfil

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
            v1 = User.objects.get(email=f'{email_variavel}').username
            user = authenticate(username=f'{v1}', password=f'{senha_variavel}')
            if user:
                login(request, user)
                resposta = user
                # if request.user.is_authenticated:
                return render(request, 'html/Perfil.html')
            else:
                request.session['erro'] = "Login invalido"
        
    
            return redirect("../")
        except User.DoesNotExist:
             request.session['erro'] = "Login invalido"
             return redirect("../")

    
def logout(request):
    auth.logout(request)
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
        send_mail(subject, message, 'django.core.mail.backends.console.EmailBackend', [reset_url] ,[user.email])

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





