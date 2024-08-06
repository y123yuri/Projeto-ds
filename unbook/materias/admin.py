from django.contrib import admin
from .models import *

admin.site.register(Professor)
admin.site.register(Materia)
admin.site.register(Turma)
admin.site.register(Comentario)
admin.site.register(Report)
admin.site.register(Resumo)
admin.site.register(Video)
admin.site.register(Atividade)
admin.site.register(Comentario_deletado)
admin.site.register(Comentario_editado)
admin.site.register(Info_semestre)