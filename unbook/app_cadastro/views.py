from django.shortcuts import render
from .forms import CadastroForm
from django.http import HttpResponse
from .models import Cadastro

# Create your views here.

def cadastro(request):
    context = {}
    form = CadastroForm()
    context["form"] = form
    return render(request, "html/cadastro.html", context)

def sucesso(request):
    obj = Cadastro()
    f = CadastroForm(request.POST, instance=obj)
    context = {}
    if f.is_valid():
        
        print(type(f), type(f.cleaned_data), type(obj))
        context["resposta"] = f.cleaned_data
        obj.save()
    else:
        context["resposta"] = False
    
    return render(request, "html/cadastro_sucesso.html", context)