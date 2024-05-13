from selenium import webdriver
from selenium.webdriver.support.select import Select

link = 'https://sigaa.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino'
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get(link)

try:
    driver.find_element("xpath", "/html/body/dialog/button").click() #cookie ciente
except:
    pass

unidade_elemento = driver.find_element("xpath", '//*[@id="formTurma:inputDepto"]')
unidade_select = Select(unidade_elemento)
unidade_select.select_by_index(78)
busca = driver.find_element("xpath", '/html/body/div/div/div[2]/form/table/tfoot/tr/td/input[1]')
busca.click()


tabela = driver.find_element("xpath", '/html/body/div/div/div[2]/form/div[2]/table')
rows = tabela.find_elements("tag name", "tr")
materia = ''
turmas_lista = []
professores = []
turma = {"materia":'', "professor":"", "turno":'', "local":""}
for linha in rows[1:-1]:
    print("-="*25)
    if linha.get_attribute("class") == "agrupador": # MATÉRIA
        print(linha.text)
        materia = linha.text.split(" ")[0]
        professores = []
    
    else: #turma
        info = linha.find_elements('tag name', 'td') # n°turma/periodo/nome_prof/horario/quantvagas/quantvagasOcupadas/local
        if '(' in info[2].text:
            info[2] = info[2].text[:info[2].text.index('(')-1]
        else:
            info[2] = info[2].text

        if info[2] not in professores:
            professores.append(info[2])
            turma["professor"] = info[2]
            turma['materia'] = materia
            turma['local'] = info[7].text
            turma['turno'] = info[3].text
            turmas_lista.append(turma.copy())
            turma = {"materia":'', "professor":"", "turno":'', "local":""}
    
        
        
            
        

        