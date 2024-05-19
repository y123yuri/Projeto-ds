
from django import forms
from .models import *


class PesquisaForm(forms):
    termo_busca = forms.CharField(max_length=100)

