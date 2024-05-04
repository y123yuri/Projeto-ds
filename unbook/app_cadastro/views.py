from django.shortcuts import render

# Create your views here.

def cadastro(request):
    return render(request, "html/cadastro.html")

def sucesso(request):
    return render(request, "html/cadastro_sucesso.html", {})