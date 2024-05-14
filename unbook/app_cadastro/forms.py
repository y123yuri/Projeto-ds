from django.forms import DateInput, ModelForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class CadastroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.fields['nome_usuario'].widget.attrs = {'class':"campoEscrito , required", "id":"CampoNome", "name":"Nome", "type":"text", "placeholder":"Usuario"}
        self.fields['email'].widget.attrs = {"class":"campoEscrito , required", "name":"Email", "type":"email", "placeholder":"Matrícula@aluno.unb.com"}
        self.fields['senha'].widget = forms.PasswordInput()
        self.fields['senha'].widget.attrs = {"class":"campoEscrito , required",  "name":"Senha", "type":"password", "placeholder":"*******"}

    class Meta:
        model = Cadastro
        fields = ['nome_usuario', 'email', 'senha']

