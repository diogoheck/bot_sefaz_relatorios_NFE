from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time


def excecao_navegador(funcao, driver, *args, **kwargs):
    for _ in range(kwargs.get('segundos', 10)):
        try:
            funcao(driver, *args)
            break

        except ElementNotInteractableException as e:
            print('Retry in 1 second', e, funcao.__name__)
            time.sleep(1)

        except NoSuchElementException as e:
            print('Retry in 1 second', e, funcao.__name__)
            time.sleep(1)
