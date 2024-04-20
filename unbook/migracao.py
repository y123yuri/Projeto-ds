from members.models import Member 
from members.models import Member 
from members.models import Member 
from members.models import Member 
from members.models import Member 
import manage


lista_materia = []
for linha_materia in tabela_excel:
    ob_materia = Materia(codigo="123", nome='teste')
    lista_materia.append(ob_materia)

for x in lista_materia:
    x.save()

ob_professor = professor(codigo="123", nome='teste')
lista_professor
for x in lista_professor:
    x.save()

ob_professor = Turma(codigo="123", nome='teste', professor="nome_professor", materia="codigo")
lista_professor = []
for x in lista_professor:
    x.save()