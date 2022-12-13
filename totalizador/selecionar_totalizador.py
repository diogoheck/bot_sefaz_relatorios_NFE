from classe_acessos import Path
from selenium.webdriver.common.by import By

def selecionar_box_totalizador(navegador):
    if not navegador.find_element(By.XPATH, Path.BOX_TOTALIZADO).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_TOTALIZADO).click()


def desmarcar_box_totalizador(navegador):
    if navegador.find_element(By.XPATH, Path.BOX_TOTALIZADO).is_selected():
        navegador.find_element(By.XPATH, Path.BOX_TOTALIZADO).click()
