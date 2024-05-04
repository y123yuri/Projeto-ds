from django import forms
from .models import *


class CadastroForms(forms.ModelForm):
    class Meta():
        model = Cadastro
        fields = ["nome_usuario", "email", "senha"]
    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('nome_usuario', css_class='campoEscrito', id="CampoNome", placeholder="Usuario"),
        Field('email', css_class='campoEscrito', name="Email", placeholder="Matrícula@aluno.unb.com"),
        Field('senha', css_class='campoEscrito', name="Senha", type="password",  placeholder="*******"),
        
    )
