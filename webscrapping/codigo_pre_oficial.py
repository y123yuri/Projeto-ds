import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import openpyxl as xls
from openpyxl.utils.dataframe import dataframe_to_rows

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

carga_horaria_lista.append('')
#não tirar esse append



options2 = webdriver.FirefoxOptions()
options2.page_load_strategy = 'eager'
fire= webdriver.Firefox(options=options2)
fire.get("https://sigaa.unb.br/sigaa/public/docente/busca_docentes.jsf?aba=p-academico")
fire.find_element(By.XPATH, '//*[@id="form:departamento"]').click()
fire.find_element(By.XPATH, "/html/body/div/div/div[2]/form/table/tbody/tr[2]/td/select/option[79]").click()
fire.find_element(By.XPATH, '//*[@id="form:buscar"]').click()
fire.minimize_window


#Pegando os Nomes
nomes = fire.find_elements(By.CLASS_NAME, 'nome')
listaNome = []
for j in nomes:
    listaNome.append(j.text)
    
#Pegando as Imagens
IMGS = []
index = 0
LFotos = []
fotos = fire.find_elements(By.TAG_NAME, 'img')
for i in fotos:
    LFotos.append(i.get_attribute('src'))
LFotos.remove(LFotos[0])

#Associando Imagens aos Nomes
while index != len(listaNome):
    #print(listaNome[index])
    if LFotos[index] == "https://sigaa.unb.br/sigaa/img/no_picture.png":
        p = listaNome[index]
        Nome1 = p.lower()
        Nome2 = Nome1.replace(" ", "-") 
        fire.get(f"https://pesquisar.unb.br/professor/{Nome2}")
        index += 1
        
        try:
            h2 = fire.find_element(By.TAG_NAME, "h2")
            if h2.is_displayed():
                img = fire.find_element(By.TAG_NAME, "img")
                IMGS.append(img.get_attribute('src')) 
        except NoSuchElementException:
            IMGS.append("https://sigaa.unb.br/sigaa/img/no_picture.png")
            print(f"A pagina do professor: {Nome2} nao existe!")
        except Exception as e:
            IMGS.append("https://sigaa.unb.br/sigaa/img/no_picture.png")
            print(f"Ocorreu um erro: {e}")

    else:
        IMGS.append(LFotos[index])
        index += 1
fire.close()





indices_encontrados = []
lista_numero_professor=[]

#pegando posicoes ''
for index, elemento in enumerate(carga_horaria_lista):
    if elemento == '':
        indices_encontrados.append(index)

i = 0
lista_lista = []
POS1 = 0
POS2 = 1

#criando lista de listas
while i != 466:
    try:
        pos1 = indices_encontrados[POS1]
        pos2 = indices_encontrados[POS2]
        lista_lista.append(carga_horaria_lista[pos1:pos2])
        POS1 += 1
        POS2 += 1
        i += 1
    except IndexError:
        i += 1

#removendo os ''
for o in lista_lista:
    del o[0]

for o in codigo_lista:
    if o == '':
        codigo_lista.remove(o)

for o in materia_lista:
    if o == '':
        materia_lista.remove(o)

for o in carga_horaria_lista:
    if o == '':
        carga_horaria_lista.remove(o)

nomes_multiplicados = []
fotos_multiplicadas=[]
contador = 0
contador1 = 0
contador67=0

#multiplicando nomes pela carga horaria
for sublist in lista_lista:
    for _ in sublist:
        nomes_multiplicados.append(nomes_lista[contador1])
    contador1 += 1

for sublist in lista_lista:
    for _ in sublist:
        fotos_multiplicadas.append(IMGS[contador67])
    contador67 += 1

coluna=['Matérias']


excel_dados=pd.DataFrame(data=materia_lista,index=nomes_multiplicados,columns=coluna)
excel_dados['Códigos']=codigo_lista
excel_dados['Carga horária']=carga_horaria_lista
excel_dados['Fotografias']=fotos_multiplicadas
excel_dados['Semestre']='2024.1'

wb = xls.Workbook()
ws = wb.active

#excel_dados.to_excel()
print('')
print(excel_dados)
print('')

for r in dataframe_to_rows(excel_dados, index=True, header=True):
    ws.append(r)

wb.save("pandas_openpyxl.xlsx")

# print(materia_lista)
# print('')
# print(carga_horaria_lista)
# print('')
# print(codigo_lista)
# print('')
# print(nomes_multiplicados)