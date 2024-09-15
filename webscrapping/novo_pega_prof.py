from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
link = 'https://sigaa.unb.br/sigaa/public/docente/busca_docentes.jsf'
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)
driver.get(link)


try:
    driver.find_element("xpath", "/html/body/dialog/button").click() #cookie ciente
except:
    pass

unidade_elemento = driver.find_element("xpath", '//*[@id="form:departamento"]')
unidade_select = Select(unidade_elemento)
prof_lista = []

for op in range(0,len(unidade_select.options)):
    start_time = time.time()
    unidade_elemento = driver.find_element("xpath", '//*[@id="form:departamento"]')
    unidade_select = Select(unidade_elemento)
    unidade_select.select_by_index(op)
    busca = driver.find_element("xpath", '//*[@id="form:buscar"]')
    busca.click()
    try:
        tabela = driver.find_element("xpath", '/html/body/div/div/div[2]/table')
    except:
        tabela = False
    if tabela:
        rows = tabela.find_elements("tag name", "tr")
        for linha in rows[1:-1]:
            info = linha.find_elements('tag name', 'td') #foto/nome
            imagem = info[0].find_element('tag name', "img").get_attribute("src")
            nome = info[1].find_element('tag name', 'span').text
            print('--'*25)
            print([nome, imagem])
            prof_lista.append([nome, imagem])

        
    print('-=-=-=-=-='*15)
    unidade_elemento = driver.find_element("xpath", '//*[@id="form:departamento"]')
    unidade_select = Select(unidade_elemento)
    print(unidade_select.options[op].text)
    print("--- %s seconds ---" % (time.time() - start_time))

with open("turmas.txt", 'w') as fp:
    for prof in prof_lista:
        fp.write('$'.join(prof))
        fp.write('\n')