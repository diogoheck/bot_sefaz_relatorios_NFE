from classe_acessos import Path
from selenium.webdriver.common.by import By

def selecionar_modelo_documentos(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_NFe).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NFe).click()
    if not navegador.find_element(By.XPATH, Path.BOX_NFCe).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NFCe).click()


def selecionar_modelo_documentos_somente_NFE(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_NFe).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NFe).click()
    if navegador.find_element(By.XPATH, Path.BOX_NFCe).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NFCe).click()
