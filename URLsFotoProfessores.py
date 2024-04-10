from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


#Entrando na Pagina dos Professores
options = webdriver.FirefoxOptions()
options.page_load_strategy = 'eager'
fire= webdriver.Firefox(options=options)
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
    print(listaNome[index])
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

#juntar nomes e fotos
junto = 0
while junto != 133:
    print(f"{IMGS[junto]} - {listaNome[junto]}")
    junto +=1 
