from classe_acessos import Path
from selenium.webdriver.common.by import By

def selecionar_notas_saidas(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_NF_SAIDAS).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NF_SAIDAS).click()


def selecionar_notas_compras(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_NF_COMPRAS).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NF_COMPRAS).click()


def selecionar_notas_proprias(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_NF_PROPRIAS).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NF_PROPRIAS).click()


def selecionar_notas_terceiros(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_NF_TERCEIROS).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_NF_TERCEIROS).click()
