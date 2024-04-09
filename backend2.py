import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#driver.get('https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673')
link='https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}
requisição=requests.get(link, headers=headers)
site=BeautifulSoup(requisição.text, "html.parser")
matérias = site.find_all("span", class_="pagina")
#link de cada professor e matéria
driver = webdriver.Firefox()

for materia in matérias:
    materia =str(materia)
    link_editado= materia.replace('<a href="','')
    link_editado2=link_editado.replace('" target="_blank" title="Clique aqui para acessar a página pública deste docente">','')
    link_editado3=link_editado2.replace('Ver página','')
    link_editado4=link_editado3.replace('</a>','')
    link_editado5=link_editado4.replace('</span>','')
    link_editado6=link_editado5.replace('<span class="pagina">','')
    print(link_editado6)
    
    
    driver.get(f'https://sigaa.unb.br{link_editado6}')
    try: #if (error)
        driver.find_element("xpath", '/html/body/dialog/button').click() # 
    except:
        pass
    driver.find_element("xpath", '/html/body/div/div/div[2]/div[1]/ul/li[3]/a').click() #esse é pra abrir a pagina disciplinas ministradas
    driver.find_element("xpath", '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[6]/a[2]/em/span').click() #clicar em graduação

    time.sleep(5)
    

    site_bs4 = BeautifulSoup(driver.page_source, "html.parser")
    tabela = site_bs4.find("table", attrs={'class':'listagem'})
    
    codigo_materia= tabela.find_all("td", class_="codigo")
    
    todas_as_informacoes = tabela.find_all("td")
    contador = 0
    while True:
        if len(todas_as_informacoes[contador].text) == 1:
            break
        else:
            print(todas_as_informacoes[contador].text)
            contador += 1
