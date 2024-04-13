import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException



#driver.get('https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673')
link='https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}
requisição=requests.get(link, headers=headers)
site=BeautifulSoup(requisição.text, "html.parser")
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'eager'
matérias = site.find_all("span", class_="pagina")
nome_professor= site.find_all("span", class_="nome")
#link de cada professor e matéria
driver = webdriver.Firefox(options=options)


contador_2 = 0
dados_sigaa=[]
materia_lista = []
codigo_lista = []
carga_horaria_lista = []
nomes_lista=[]


for i in nome_professor:
    nomes=i.text
    nomes_editados1=nomes.replace('(DOUTOR)','')
    nomes_editados2=nomes_editados1.replace('(ESPECIALISTA)','')
    nomes_editados3=nomes_editados2.replace('(MESTRE)','')
    nomes_editados3
    #print(nomes_editados3.strip())
    
    nomes_lista.append(nomes_editados3.strip())




for materia in matérias:
    materia =str(materia)
    link_editado= materia.replace('<a href="','')
    link_editado2=link_editado.replace('" target="_blank" title="Clique aqui para acessar a página pública deste docente">','')
    link_editado3=link_editado2.replace('Ver página','')
    link_editado4=link_editado3.replace('</a>','')
    link_editado5=link_editado4.replace('</span>','')
    link_editado6=link_editado5.replace('<span class="pagina">','')
    #print(link_editado6)
    
    driver.get(f'https://sigaa.unb.br{link_editado6}')
    try: #if (error)
        driver.find_element("xpath", '/html/body/dialog/button').click() # 
    except NoSuchElementException:
        pass
    driver.find_element("xpath", '/html/body/div/div/div[2]/div[1]/ul/li[3]/a').click() #esse é pra abrir a pagina disciplinas ministradas
    driver.find_element("xpath", '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[6]/a[2]/em/span').click() #clicar em graduação


    site_bs4 = BeautifulSoup(driver.page_source, "html.parser")
    tabela = site_bs4.find("table", attrs={'class':'listagem'})
    
    codigo_materia= tabela.find_all("td", class_="codigo")
    
    todas_as_informacoes = tabela.find_all("td")
    
    contador = 0
    while True: # Separa todos os codigos, materias, carga horario do semestre atual de cada professor
        if contador_2 == 128:
            for i in todas_as_informacoes:
                dados_sigaa.append(i.text) # Corrige o problema do professor novato
            break
        if contador_2 == 129:
            for i_2 in todas_as_informacoes:
                dados_sigaa.append(i_2.text)
            break
        if contador_2 == 132:
            for i_3 in todas_as_informacoes:
                dados_sigaa.append(i_3.text)
            break
        if contador_2 == 133:
            for i_4 in todas_as_informacoes:
                dados_sigaa.append(i_4.text)
            break
        if len(todas_as_informacoes[contador].text) == 1:
            break
        else:
            print(todas_as_informacoes[contador].text)
            dados_sigaa.append(todas_as_informacoes[contador].text)
            contador += 1
            
    contador_2 += 1 

dados_sigaa.append('')
contador_3 = 0
while True: # Cria listas de todos os codigos, materias, carga horario (separadamente) de todos os professores em ordem
    if len(dados_sigaa[contador_3]) == 0:
        break
    else:
        if len(dados_sigaa[contador_3])== 7:     
            pass
            #print(f'Semestre:{dados_sigaa[contador2]}')
            codigo_lista.append('')
            carga_horaria_lista.append('')
            materia_lista.append('')

        elif len(dados_sigaa[contador_3]) == 9:
            codigo_lista.append(dados_sigaa[contador_3])
            #print(f'Código:{dados_sigaa[contador2]}')
    
        elif len(dados_sigaa[contador_3]) == 5:
            carga_horaria_lista.append(dados_sigaa[contador_3])
            #print(f'Carga Hóraria:{dados_sigaa[contador2]}')

        else:
            materia_lista.append(dados_sigaa[contador_3])
            #print(f'Máteria:{dados_sigaa[contador2]}')
                   
        contador_3 += 1


print(materia_lista)
print('')
print(carga_horaria_lista)
print('')
print(codigo_lista)
print('')