from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.http import HttpResponse
from .models import Cadastro
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    context = {}
    form = CadastroForm()
    context["form"] = form
    if request.method == "POST":
        context['erro'] = "já existe um cadastro com o email ou nome de usuario"
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
    return render(request, "html/Login.html")

def esqueceu(request):
    return render (request, "html/Nova_senha_email.html")
    
def novaSenha(request):
    return render(request, "html/Nova_senha.html")