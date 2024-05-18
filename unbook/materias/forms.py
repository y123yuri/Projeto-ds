
from django import forms
from .models import *


class PesquisaForm(forms):
    termo_busca = forms.CharField(max_length=100)

class Avaliacao_tudaoForm(modelForm):
    def __init__(self, *args, **kwargs):
        super(Avaliacao_tudaoForm, self).__init__(*args, **kwargs)
        self.fields