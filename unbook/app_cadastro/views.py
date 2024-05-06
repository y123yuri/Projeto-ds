from django.shortcuts import render
<<<<<<< HEAD
from .forms import CadastroForm
from django.http import HttpResponse
from .models import Cadastro
=======
from forms import CadastroForms
>>>>>>> 098859d47ef34f5d02a0d1fbb6c0a66ccd05f8c4

# Create your views here.

def cadastro(request):
    context = {}
<<<<<<< HEAD
    form = CadastroForm()
=======
    form = CadastroForms()
>>>>>>> 098859d47ef34f5d02a0d1fbb6c0a66ccd05f8c4
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