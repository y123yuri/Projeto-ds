from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time
link = 'https://sigaa.unb.br/sigaa/public/docente/busca_docentes.jsf'
#link2 = 'https://pesquisar.unb.br/professor/{nome_professor}'
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)
driver.get(link)
#Criando as tabs necessárias
pg1 = driver.current_window_handle #tab da variável link
driver.switch_to.new_window('tab')
pg2 = driver.current_window_handle #tab da variável link2 
driver.switch_to.window(pg1)


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
            nome = info[1].find_element('tag name', 'span').text
            imagem = info[0].find_element('tag name', "img").get_attribute("src")
            if imagem == 'https://sigaa.unb.br/sigaa/img/no_picture.png': #caso não tenha imagem, pesquisar no site pesquisa Unb
                nome_professor = info[1].find_element('tag name', 'span').text #tratando o nome para inserir no link
                nome_professor = nome_professor.replace(' ', '-') 
                nome_professor = nome_professor.lower()
                try:
                    driver.switch_to.window(pg2) #troca para a tab de pesquisa
                    driver.get(f'https://pesquisar.unb.br/professor/{nome_professor}')
                    imagem = driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div[1]/img').get_attribute("src") #insere a imagem no lugar da anterior (sem imagem)
                    driver.switch_to.window(pg1)
                except NoSuchElementException:
                    print('Foto nÃ£o existe!')
                    imagem == 'https://sigaa.unb.br/sigaa/img/no_picture.png' #caso não exista a página bota a imagem padrão de sem imagem
                    driver.switch_to.window(pg1)
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