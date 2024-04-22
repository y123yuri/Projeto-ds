
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


print(lista_nomeprofessor_codigo)
print('')
print(lista_nomeprofessor_foto)
print('')
print(lista_codigo_nomemateria_cargahoraria)