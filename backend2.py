import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
#driver.get('https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673')
link='https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
requisição=requests.get(link, headers=headers)
site=BeautifulSoup(requisição.text, "html.parser")
matéria= site.find_all("span", class_="pagina")
#link de cada professor e matéria

for c in matéria:
    c=str(c)
    link_editado=c.replace('<a href="','')
    link_editado2=link_editado.replace('" target="_blank" title="Clique aqui para acessar a página pública deste docente">','')
    link_editado3=link_editado2.replace('Ver página','')
    link_editado4=link_editado3.replace('</a>','')
    link_editado5=link_editado4.replace('</span>','')
    link_editado6=link_editado5.replace('<span class="pagina">','')
    print(link_editado6)
    
    driver = webdriver.Firefox()
    driver.get(f'https://sigaa.unb.br{link_editado6}')
    driver.find_element("xpath", '/html/body/dialog/button').click()
    driver.find_element("xpath", '/html/body/div/div/div[2]/div[1]/ul/li[3]/a').click()
    #esse é pra abrir a pagina disciplinas ministradas
    driver.find_element("xpath", '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[6]/a[2]/em/span').click()
    #clicar em graduação



    link2=(f'https://sigaa.unb.br{link_editado6}')
    headers2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    requisição2=requests.get(link2, headers=headers)
    site_bs4=BeautifulSoup(requisição.text, "html.parser")
    codigo_materia=site.find_all("td", class_="codigo")
    #disciplina_ministrada=site.find_all("a", name="href")
    print(f'{codigo_materia}','6')
    
