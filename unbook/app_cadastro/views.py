from django.shortcuts import render

# Create your views here.

def cadastro(request):
    return render(request, "app_cadastro/cadastro.html")