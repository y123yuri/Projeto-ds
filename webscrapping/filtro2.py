comentario_usuario = 'yoko e mae'
#comentario_usuario = 'essa professora de merda me reprovou, é uma vagabunda do caralhop, puta sem mae'

lista_proibida = ['merda', 'porra', 'caralho', 'buceta', 'puta', 'foda-se', 'cacete', 'desgraça', 'vagabunda', 'filho da puta', 'arrombado', 'viado', 'cu', 'pau no cu',
'piranha', 'puta que pariu', 'puta merda', 'pqp', 'babaca', 'cuzão', 'escroto', 'fdp', 'bosta', 'fudido', 'caralha', 'corno', 'fudido', 'retardado', 'biscate',
'bicha', 'boquete', 'vagabundo', 'meretriz', 'arrombada', 'boiola', 'cabrão', 'chupa', 'escrota', 'trouxa', 'otário', 'xota', 'xoxota', 'zorra', 'cabrona',
'puta que te pariu', 'caralho de asa', 'filha da puta', 'cornudo', 'caralhudo', 'escrotão', 'filho da mãe', 'fode', 'maldito', 'jumento', 'panaca', 'retardado',
'paspalho', 'mané', 'boceta', 'trouxa', 'besta', 'ralé', 'meretriz', 'chupa rola', 'rola', 'puta velha', 'chifrudo', 'bostinha', 'merdinha', 'cagão', 'boiolinha',
'lixo', 'merdoso', 'bundão', 'lambisgóia', 'fedido', 'pau mole', 'pinto', 'pintudo', 'rabo', 'rabo de saia', 'safado', 'sem-vergonha', 'vagaba', 'bobo da corte',
'espermatozóide', 'cuspidor', 'coxinha', 'cabaço', 'fedorento', 'peido', 'peidão', 'vagabundinho', 'esquema', 'casca de ferida', 'bagulho', 'mentecapto', 'caga-regra',
'saco', 'saco cheio', 'filho do capeta', 'inferno', 'tornozelo', 'babaca', 'panaca', 'fela da puta']

comentario_split = comentario_usuario.split(' ')
print(comentario_split)
novo_comentario = []
for palavra in comentario_split: #pega todas as palavras
    if palavra in lista_proibida:
        contador = 0
        for letra in palavra:
            contador += 1
        palavra = contador * '*'
    novo_comentario.append(palavra)
    comentario_usuario.join(novo_comentario)
print(comentario_usuario)
    # else:
    #     comentario_usuario = comentario_usuario
    #     print(comentario_usuario)