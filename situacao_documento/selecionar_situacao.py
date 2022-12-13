from classe_acessos import Path
from selenium.webdriver.common.by import By

def selecionar_situacao_documento_normal(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_SIT_NORMAL).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_SIT_NORMAL).click()
    if navegador.find_element(By.XPATH, Path.BOX_SIT_CANCEL).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_SIT_CANCEL).click()


def selecionar_situacao_documento_cancelada(navegador):
    if navegador.find_element(By.XPATH, Path.BOX_SIT_NORMAL).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_SIT_NORMAL).click()
    if not navegador.find_element(By.XPATH, Path.BOX_SIT_CANCEL).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_SIT_CANCEL).click()
