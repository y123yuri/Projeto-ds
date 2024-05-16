from django.shortcuts import render, redirect
from .forms import CadastroForm
from .forms import LoginForm
from django.http import HttpResponse
from .models import Cadastro
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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
        
    else:
        request.session['erro'] = "já existe um cadastro com o email ou nome de usuario"
        return redirect("../")
    return render(request, "html/cadastro_sucesso.html", context)

def login(request):
    context = {}
    form = LoginForm()
    context["form"] = form
    print(context)
    return render(request, "html/Login.html", context)

def logado(request):
    f = LoginForm(request.POST)
    context = {}
    if 'erro' in request.session:
        del request.session['erro']

    if f.is_valid():
        context["resposta"] = f.cleaned_data
        dados = context['resposta']
        email_variavel = dados ['email']
        senha_variavel = dados ['password']
        dados = [email_variavel, senha_variavel] #tratamento de dados
        user = authenticate(email=dados[0], password=dados[1])

        print(dados)
        print(user)
        
    if user:
        login(request, user)
        # if request.user.is_authenticated:
        return HttpResponse('logado')
    else:
        request.session['erro'] = "Login invalido"
        return redirect("../")
            
    
    
def esqueceu(request):
    return render (request, "html/Nova_senha_email.html")
    
def novaSenha(request):
    return render(request, "html/Nova_senha.html")