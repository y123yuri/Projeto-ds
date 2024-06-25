comentario_usuario = 'yoko e mae a minha rola'

import re

lista_proibida = ['merda', 'porra', 'caralho', 'buceta', 'puta', 'foda se', 'cacete', 'desgraça', 'vagabunda', 'filho da puta', 'arrombada', 'viado', 'cu', 'pau no cu', 'piranha', 'puta que pariu', 'puta merda', 'pqp', 'babaca', 'cuzão', 'escroto', 'fdp', 'bosta', 'fudido', 'caralha', 'corno', 'fudido', 'retardado', 'biscate', 'bicha', 'boquete', 'vagabundo', 'meretriz', 'arrombada', 'boiola', 'cabrão', 'chupa', 'escrota', 'trouxa', 'otário', 'xota', 'xoxota', 'zorra', 'cabrona', 'puta que te pariu', 'caralho de asa', 'filha da puta', 'cornudo', 'caralhudo', 'escrotão', 'filho da mãe', 'fode', 'maldito', 'jumento', 'panaca', 'retardado', 'paspalho', 'mané', 'boceta', 'trouxa', 'besta', 'ralé', 'meretriz', 'chupa rola', 'rola', 'puta velha', 'chifrudo', 'bostinha', 'merdinha', 'cagão', 'boiolinha', 'lixo', 'merdoso', 'bundão', 'lambisgóia', 'fedido', 'pau mole', 'pinto', 'pintudo', 'rabo', 'rabo de saia', 'safado', 'sem-vergonha', 'vagaba', 'bobo da corte', 'espermatozóide', 'cuspidor', 'coxinha', 'cabaço', 'fedorento', 'peido', 'peidão', 'vagabundinho', 'esquema', 'casca de ferida', 'bagulho', 'mentecapto', 'caga-regra', 'saco', 'saco cheio', 'filho do capeta', 'inferno', 'tornozelo', 'babaca', 'panaca', 'fela da puta', 'fuder', 'velha', 'foder', 'sexo', 'fds', 'africano', 'aleijado', 'analfabeto', 'anus', 'anão', 'apenado', 'baba-ovo', 'babaca', 'babaovo', 'bacura', 'bagos', 'baianada', 'baitola', 'barbeiro', 'barraco', 'beata', 'bebum', 'besta', 'bicha', 'bisca', 'bixa', 'boazuda', 'boceta', 'boco', 'boiola', 'bolagato', 'bolcat', 'boquete', 'bosseta', 'bosta', 'bostana', 'branquelo', 'brecha', 'brexa', 'brioco', 'bronha', 'buca', 'buceta', 'bugre', 'bunda', 'bunduda', 'burra', 'burro', 'busseta', 'bárbaro', 'bêbado', 'cachorra', 'cachorro', 'cadela', 'caga', 'cagado', 'cagao', 'cagona', 'caipira', 'canalha', 'canceroso', 'caralho', 'casseta', 'cassete', 'ceguinho', 'checheca', 'chereca', 'chibumba', 'chibumbo', 'chifruda', 'chifrudo', 'chochota', 'chota', 'chupada', 'chupado', 'ciganos', 'clitoris', 'cocaina', 'coco', 'comunista', 'corna', 'corno', 'cornuda', 'cornudo', 'corrupta', 'corrupto', 'coxo', 'cretina', 'cretino', 'crioulo', 'cruz-credo', 'cu', 'culhao', 'curalho', 'cuzao', 'cuzuda', 'cuzudo', 'debil', 'debiloide', 'deficiente', 'defunto', 'demonio', 'denegrir', 'detento', 'difunto', 'doida', 'doido', 'egua', 'elemento', 'encostado', 'esclerosado', 'escrota', 'escroto', 'esporrada', 'esporrado', 'esporro', 'estupida', 'estupidez', 'estupido', 'fanático', 'fascista', 'fedida', 'fedido', 'fedor', 'fedorenta', 'feia', 'feio', 'feiosa', 'feioso', 'feioza', 'feiozo', 'felacao', 'fenda', 'foda', 'fodao', 'fode', 'fodida', 'fodido', 'fornica', 'fornição', 'fudendo', 'fudeção', 'fudida', 
'fudido', 'furada', 'furado', 'furnica', 'furnicar', 'furo', 'furona', 'furão', 'gaiata', 'gaiato', 'gay', 'gilete', 'goianada', 'gonorrea', 'gonorreia', 'gosmenta', 'gosmento', 'grelinho', 'grelo', 'gringo', 'homo-sexual', 'homossexual', 'homossexualismo', 'idiota', 'idiotice', 'imbecil', 'inculto', 'iscrota', 'iscroto', 'japa', 'judiar', 'ladra', 'ladrao', 'ladroeira', 'ladrona', 'ladrão', 'lalau', 'lazarento', 'leprosa', 'leproso', 'louco', 'lésbica', 'macaca', 'macaco', 'machona', 'macumbeiro', 'malandro', 'maluco', 'maneta', 'marginal', 'masturba', 'meleca', 'meliante', 'merda', 'mija', 'mijada', 'mijado', 'mijo', 'minorias', 'mocrea', 'mocreia', 'moleca', 'moleque', 'mondronga', 'mondrongo', 'mongol', 'mulato', 'naba', 'nadega', 'nazista', 'negro', 'nojeira', 'nojenta', 'nojento', 'nojo', 'olhota', 'otaria', 'otario', 'otária', 'otário', 'paca', 'palhaço', 'paspalha', 'paspalhao', 'paspalho', 
'pau', 'peia', 'peido', 'pemba', 'pentelha', 'pentelho', 'perereca', 'perneta', 'peru', 'peão', 'pica', 'picao', 'pilantra', 'pinel', 'piranha', 'piroca', 'piroco', 'piru', 'pivete', 'político', 'porra', 'prega', 'preso', 'prost-bulo', 'prostibulo', 'prostituta', 'prostituto', 'punheta', 'punhetao', 'pus', 'pustula', 'puta', 'puto', 'puxa-saco', 'puxasaco', 'pênis', 'rabao', 'rabo', 'rabuda', 'rabudao', 'rabudo', 'rabudona', 'racha', 'rachada', 'rachadao', 'rachadinha', 'rachadinho', 'rachado', 'ramela', 'remela', 'retardada', 'retardado', 'ridícula', 'roceiro', 'rola', 'rolinha', 'rosca', 'sacana', 'safada', 'safado', 'sapatao', 'sapatão', 'sifilis', 'siririca', 'tarada', 'tarado', 'testuda', 'tezao', 'tezuda', 'tezudo', 'traveco', 'trocha', 'trolha', 'troucha', 'trouxa', 'troxa', 'tuberculoso', 'tupiniquim', 'turco', 'vaca', 'vadia', 'vagabunda', 'vagabundo', 'vagina', 'veada', 'veadao', 'veado', 
'viada', 'viadao', 'víado', 'xana', 'xaninha', 'xavasca', 'xerereca', 'xexeca', 'xibiu', 'xibumba', 'xiíta', 'xochota', 'xota', 'xoxota', 'bebum', 'bêbedo', 'denigrir', 'leproso', 'mongolóide', 'índio']

novo_comentario = []

filtragem = re.split(r"\s", comentario_usuario) # separa cada palavra

print(filtragem, 'filtragem')

arg = 0
for c in filtragem: #deixando tudo minusculo
    filtragem[arg] = filtragem[arg].lower()

for i in filtragem: #FILTRO PRINCIAPA
    arg += 1
    if i in lista_proibida: #esta na lista
        print('Na lista')
        try:
            censura = re.sub(r"\w", "*", i) #censura
            filtragem[filtragem.index(i)] = censura
        except ValueError:
            print('Já filtrou')
        
    else:
        if re.search("[0-9]", i): #tem numero ou caractere na palavra
            print('Tem numero ou caractere', i)
            val = list(i)
            for c in val:
                if c.isdigit():
                    index = val.index(c) # posicao numero
                    val = ''.join(val[0:index]) # inicio ate o numero
                    val1 = ''.join(val[index::]) #numero ate o final
                    for a in lista_proibida:
                        if re.search(f"^{val}.*{val1}", a):
                            print('Filtro Numero', a)
                            try:
                                censura = re.sub(r"\w", "*", i) #censura
                                filtragem[filtragem.index(i)] = censura
                            except ValueError:
                                print('Já filtrou')
        else:
            val = list(i)
            val = val[:4]
            palavra = ''.join(val)
            print(palavra) # encontrar palavra parecida na lista
            for a in lista_proibida:
                if re.search(fr"\A{palavra}", a):
                    print('Filtro Sem Numero', a)
                    try:
                        censura = re.sub(r"\w", "*", i) #censura
                        filtragem[filtragem.index(i)] = censura
                        print('censura')
                    except ValueError:
                        print('Já filtrou')
            

print(filtragem)
for b in filtragem:
    novo_comentario.append(b)
    novo_comentario.append(' ')

print(novo_comentario)
#a r r o m b a d o
