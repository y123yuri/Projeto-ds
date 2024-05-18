from django.shortcuts import render, redirect
from .forms import CadastroForm
from .forms import LoginForm
from .forms import Esqueceu_senhaForm
from django.http import HttpResponse
from .models import Cadastro
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth



# Create your views here.

def cadastro(request):
    context = {}
    form = CadastroForm()
    context["form"] = form
    return render(request, "html/cadastro.html", context)

def sucesso(request):
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
        nome_variavel = dados ['username']
        email_variavel = dados ['email']
        senha_variavel = dados ['password']
        dados = [nome_variavel, email_variavel, senha_variavel]
        user = User.objects.create_user(username=dados[0],email=dados[1],password=dados[2])
        user.save()
        #escrever autenticação
        
        
    else:
        request.session['erro'] = "já existe um cadastro com o email ou nome de usuario"
        return redirect("../")
    return render(request, "html/cadastro_sucesso.html", context)

def login_func(request):
    if not request.user.is_authenticated:
        context = {}
        form = LoginForm()
        context["form"] = form
        print(context)
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
        print(email_variavel)
    return render(request, 'html/jogadados.html', context)

    
def novaSenha(request):
    return render(request, "html/Nova_senha.html")

