from django.forms import DateInput, ModelForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class CadastroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {'class':"campoEscrito , required", 'autocomplete':"off", "name":"Nome", "type":"text", "placeholder":"Seu nome completo" , "oninput":"nomeConfirmaValidade()"}

        self.fields['username'].widget.attrs = {'class':"campoEscrito , required","id":"CampoNome", 'autocomplete':"off", "name":"Usuario", "type":"text", "placeholder":"Usuario" , "oninput":"nomeValidade()"}

        self.fields['email'].widget.attrs = {"class":"campoEscrito , required", 'autocomplete':"off", "name":"Email", "type":"email", "placeholder":"Matrícula@aluno.unb.com" , "oninput":"emailValidade()"}
    
        self.fields['password'].widget = forms.PasswordInput()
        # nn estou conseguindo o confirma senha
        self.fields['password'].widget.attrs = {"class":"campoEscrito , required",  "name":"Senha", "type":"password", "placeholder":"*******" , "oninput":"senhaValidade()"}

        self.fields['senha_confirma'].widget = forms.PasswordInput()
        # nn estou conseguindo o confirma senha
        self.fields['senha_confirma'].widget.attrs = {"class":"campoEscrito , required",  "name":"Confirm", "type":"password", "placeholder":"*******" , "oninput":"confirmasenhaValidade()"}

    class Meta:
        model = Cadastro
        fields = ['name' ,'username', 'email', 'password','senha_confirma']


class LoginForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {"class":"campoEscrito , required", "name":"Email", "type":"email", "placeholder":"Matrícula@aluno.unb.com"}
        
        self.fields['password'].widget = forms.PasswordInput()

        self.fields['password'].widget.attrs = {"class":"campoEscrito , required",  "name":"Senha", "type":"password", "placeholder":"*******"}
        
    class Meta:
        model = Cadastro 
        fields = ['email', 'password']

class Esqueceu_senhaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Esqueceu_senhaForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {"class":"campoEscrito , required", "name":"Email", "type":"email", "placeholder":"Matrícula@aluno.unb.com"}
    class Meta:
        model = Cadastro
        fields = ['email']

class Nova_senhaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Nova_senhaForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        
        self.fields['password'].widget.attrs = {"class":"campoEscrito , required",  "name":"Senha", "type":"password", "placeholder":"*******"}

    class Meta:
        model = Cadastro
        fields = ['password']

class Nova_senha_perfilForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Nova_senha_perfilForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        
        self.fields['password'].widget.attrs = {"class":"campoEscrito , required",  "name":"Senha", "type":"password", "placeholder":"*******"}

    class Meta:
        model = Cadastro
        fields = ['password']

    
class PerfilForm(ModelForm):
    def init(self, args, **kwargs):
        super(PerfilForm, self).init(args, **kwargs)
        self.fields['curso'].widget.attrs = {"class":"forms", "type":"text", "id":"curso" }
        self.fields['semestre'].widget.attrs = {"class":"forms", "type":"text", "id":"semestre" }
        self.fields['descricao'].widget.attrs = {"class":"forms", "type":"text", "id":"descricao" }

    class Meta:
        model = PerfilUsuario
        fields = ['curso', 'semestre', 'descricao']



        
