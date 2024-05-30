#pegar todas os cursos 

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


#Entrando na Pagina dos Professores
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'eager'
fire= webdriver.Firefox(options=options)
fire.get("https://www.unb.br/graduacao/cursos")
lista = fire.find_elements(By.TAG_NAME, 'li')
cursos = []
for i in lista:
    cursos.append(i.text)
pos = cursos.index("Enfermagem")
posf = cursos.index("Gestão do Agronegócio")
cursos = cursos[pos:posf+1]

cursos_lista = []

for i in cursos:
    cursos_lista.append(cursos[i])

fire.close()
print(cursos_lista)