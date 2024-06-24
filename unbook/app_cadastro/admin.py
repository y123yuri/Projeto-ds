from django.contrib import admin
from .models import *
from .models import PerfilUsuario

admin.site.register(PerfilUsuario)
admin.site.register(Cadastro)
admin.site.register(Cursos_unb)
admin.site.register(Username_trocado)