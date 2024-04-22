# from unbook.models import Professor
# from unbook.models import Materia 
# from unbook.models import Turma 
#from .models import Member 
# import manage


with open('arquivos/Nome_lista.txt','r') as arquivo:
    nomes_lista=arquivo.read().split(',')
with open('arquivos/Codigos_lista.txt','r') as arquivo:
    codigo_lista=arquivo.read().split(',')
with open('arquivos/Fotos_lista.txt','r') as arquivo:
    IMGS=arquivo.read().split(',')
with open('arquivos/Carga_horaria_lista.txt','r') as arquivo:
    carga_horaria_lista=arquivo.read().split(',')
with open('arquivos/Materia_lista.txt','r',encoding='utf-8') as arquivo:
    materia_lista=arquivo.read().split(',')
     

lista_nomeprofessor_foto = [[nomes_lista[i].strip(), IMGS[i].strip()] for i in range(min(len(nomes_lista), len(IMGS)))]

lista_codigo_nomemateria_cargahoraria = [[codigo_lista[i].strip(), materia_lista[i].strip(), carga_horaria_lista[i].strip()] for i in range(min(len(codigo_lista), len(materia_lista),len(carga_horaria_lista)))]

lista_nomeprofessor_codigo = [[nomes_lista[i].strip(), codigo_lista[i].strip()] for i in range(min(len(nomes_lista), len(codigo_lista)))]

#print(lista_codigo_nomemateria_cargahoraria)
#print("-="*25)
#print(lista_nomeprofessor_codigo)
#print("-="*25)
#print(lista_nomeprofessor_foto)

lista_turma_class = []
lista_professor_class = []
lista_materia_class = []

"""
for materia_linha in lista_codigo_nomemateria_cargahoraria: 
    ob_materia = Materia(codigo=materia_linha[0], nome=materia_linha[1], carga_horaria= materia_linha[2])
    lista_materia_class.append(ob_materia)

for x in lista_materia_class:
    x.save()

for professor_linha in lista_nomeprofessor_foto:
    ob_professor = Professor(nome=professor_linha[0], foto=professor_linha[1])
    lista_professor_class.append(ob_professor)

for y in lista_professor_class:
    y.save()

for turma_linha in lista_nomeprofessor_codigo:
    ob_turma = Turma(professor=turma_linha[0], materia=turma_linha[1], avaliação_1=0, avaliação_2=0, avaliação_3=0)
    lista_turma_class.append(ob_turma)

for z in lista_turma_class:
    z.save()
"""
