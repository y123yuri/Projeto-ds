from django.shortcuts import render
from forms import CadastroForms

# Create your views here.

def cadastro(request):
    context = {}
    form = CadastroForms()
    context["form"] = form
    return render(request, "html/cadastro.html", context)

def sucesso(request):
    return render(request, "html/cadastro_sucesso.html", {})