from classe_acessos import Path
import time
from selenium.webdriver.common.by import By

def inserir_CNPJ(navegador, CNPJ):

    navegador.find_element(By.XPATH, Path.INPUT_CNPJ).clear()
    navegador.find_element(By.XPATH, Path.INPUT_CNPJ).send_keys(CNPJ)
