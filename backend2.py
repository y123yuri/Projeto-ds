import selenium
from selenium import webdriver
from selenium import By
import requests
from bs4 import BeautifulSoup
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




    link2=(f'https://sigaa.unb.br{link_editado6[1:]}')
    print(link2)
    headers2 = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"}
    requisição2=requests.get(link2, headers=headers2)
    site_bs4 = BeautifulSoup(requisição2.text, "html.parser")
    codigo_materia= site_bs4.find_all("td", class_="codigo")
    # disciplina_ministrada=site.find_all("a", name="href")
    print(f'{codigo_materia}','6')
    break
    
