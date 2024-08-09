variavel = 0
pre_context_curtida = [3,8,2,16]
comentarios = ["a","b",'c',"d"]
contador_for = 0
pre_context = []
pre_context_curtida2=[]

seila = []
seila2= []

lista = []
for c in range(0,len(pre_context_curtida)):
    nova = [comentarios[c]],[pre_context_curtida[c]]
    lista.append(nova)

print(lista)
nova_lista=sorted(lista, reverse=True, key=lambda lista: lista[1]) 


for c in nova_lista:
    x=c[0]
    y=c[1]
    
    pre_context.append(x)
    pre_context_curtida2.append(y)

for d in pre_context:
    x= d[0]
    seila.append(x)

for e in pre_context_curtida2:
    x= e[0]
    seila2.append(x)


    
# print(seila)
# print(seila2)


