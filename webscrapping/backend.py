import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl as xls
link='https://sigaa.unb.br/sigaa/public/departamento/professores.jsf?id=673'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
requisição=requests.get(link, headers=headers)
site=BeautifulSoup(requisição.text, "html.parser")
#print(site.prettify())
nome_professor= site.find_all("span", class_="nome")
matérias = site.find_all("span", class_="pagina")
nomes_lista=[]
#essa é a lista de nomes.
for i in nome_professor:
    nomes=i.text
    nomes_editados1=nomes.replace('(DOUTOR)','')
    nomes_editados2=nomes_editados1.replace('(ESPECIALISTA)','')
    nomes_editados3=nomes_editados2.replace('(MESTRE)','')
    nomes_editados3
    #print(nomes_editados3.strip())
    
    nomes_lista.append(nomes_editados3.strip())
#print(nomes_lista)

coluna=['PROFESSORES',]
conteudo=[0,1]
excel_dados= pd.DataFrame(data=nomes_lista,index=nomes_lista,columns=coluna)

wb = xls.Workbook()
ws = wb.active

for r in dataframe_to_rows(excel_dados, index=True, header=True):
    ws.append(r)
wb.save("pandas_openpyxl.xlsx")
#cria a tabela
#excel_dados.to_excel('Nomes_professor_beta.xls')#esta dando erro
#joga no excel