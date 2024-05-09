from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.http import HttpResponse
from .models import Cadastro

# Create your views here.

def cadastro(request):
    context = {}
    form = CadastroForm()
    context["form"] = form
    if request.method == "POST":
        context['erro'] = "já existe um cadastro com o email ou nome de usuario"
    return render(request, "html/cadastro.html", context)

def sucesso(request):
    obj = Cadastro()
    f = CadastroForm(request.POST, instance=obj)
    context = {}
    if 'erro' in request.session:
        del request.session['erro']
    if f.is_valid():
        print(type(f), f.cleaned_data, type(obj))
        context["resposta"] = f.cleaned_data
        obj.save()
    else:
        request.session['erro'] = "já existe um cadastro com o email ou nome de usuario"
        return redirect("../")
    return render(request, "html/cadastro_sucesso.html", context)

def login(request):
    return render(request, "html/Login.html")