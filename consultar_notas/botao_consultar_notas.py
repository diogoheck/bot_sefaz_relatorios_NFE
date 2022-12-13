from classe_acessos import Path
import pyautogui
from teste_movimento_notas.testar_movimentacao import tem_movimento
import time
from selenium.webdriver.common.by import By

def clicar_botao_consultar_notas(navegador):

    navegador.find_element(By.XPATH, Path.BOTAO_CONSULTAR).click()

    time.sleep(5)
