from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#iniciar navegador
navegador = webdriver.Chrome()

# abrir a página index (entrar no site da busca jurídica)
pasta_script = os.path.dirname(os.path.abspath(__file__))
# monta os caminhos a partir dessa pasta
arquivo = os.path.join(pasta_script, "index.html")
arquivo = "file:///" + arquivo.replace("\\", "/")

df = pd.read_excel(os.path.join(pasta_script, "Processos.xlsx"))

#selecionando o estado
for index, row in df.iterrows():
    navegador.get(arquivo)
    menu = navegador.find_element(By.XPATH, '/html/body/div/div/button')

    #colocar o mouse sob a lista de cidades
    ActionChains(navegador).move_to_element(menu).perform()
    time.sleep(1)

    #selecionar a cidade
    cidade = row["Cidade"]
    navegador.find_element(By.PARTIAL_LINK_TEXT, cidade).click()

    #mudar para nova aba
    aba_original = navegador.window_handles[0]
    indice = 1 + index
    aba_nova = navegador.window_handles[indice]
    navegador.switch_to.window(aba_nova)

    #preencher o formulario
    navegador.find_element(By.ID, "nome").send_keys(row["Nome"])
    navegador.find_element(By.ID, "advogado").send_keys(row["Advogado"])
    navegador.find_element(By.ID, "numero").send_keys(row["Processo"])

    #clica em pesquisar
    navegador.find_element(By.CLASS_NAME, "registerbtn").click()
    time.sleep(1)

    #alerta
    alerta = Alert(navegador)
    alerta.accept()

    #espera o resultado e agir de acordo
    alerta = None
    while alerta is None:
        try:
            alerta = Alert(navegador)
            alerta.text  # força verificar se o alerta realmente existe
        except:
            alerta = None
            time.sleep(1)

    texto_alerta = alerta.text
    if "Processo encontrado com sucesso" in texto_alerta:
        alerta.accept()
        df["Status"] = "Encontrado"
    else:
        df["Status"] = "Não Encontrado"
        alerta.accept()