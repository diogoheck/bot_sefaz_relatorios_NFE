import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException


def excecao_telas(funcao):
    i = 1
    while(not funcao()):
        print(f'Retry in {i} second window 1 {funcao.__name__}')
        time.sleep(1)
        i = i + 1
