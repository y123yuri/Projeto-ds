materias =[]
with open("arquivos_txt/materias_geral.txt") as fp:
    linha = fp.readline()
    while linha:
        materia = linha.split(",")
        materia[1] = materia[1].strip()
        materias.append(materia)
        linha = fp.readline()

professores =[]
nome_prof = []
with open("arquivos_txt/professores_geral.txt") as fp:
    linha = fp.readline()
    while linha:
        professor = linha.split(",")
        professores.append(professor)
        nome_prof.append(professor[0])
        linha = fp.readline()

turmas =[]
faltando = []
with open("arquivos_txt/turmas_geral.txt") as fp:
    linha = fp.readline()
    while linha:
        turma = linha.split(",")
        if turma[1] not in nome_prof:
            faltando.append(turma)
        turmas.append(turma)
        linha = fp.readline()

print(len(faltando))
for e in range(10):
    print(faltando[e])


for turma in turmas:
    obj_prof = Professor.objects.filter(nome=turma[1])
    if not obj_prof:
            obj_prof = Professor(nome=turma[1], foto="https://sigaa.unb.br/sigaa/img/no_picture.png")
            obj_prof.save()
    else:
            obj_prof = Professor.objects.get(nome=turma[1])
    obj_materia = Materia.objects.get(codigo=turma[0])
    obj_turma = Turma(professor=obj_prof, materia=obj_materia, turno=turma[2], local=turma[3].strip(), avaliação_1=0, avaliação_2=0, avaliação_3=0)
    obj_turma.save()




