import time
from excecoes.excecao_navegador import excecao_navegador
from selenium.webdriver.common.by import By

def acessar_servicos(navegador):
    navegador.find_element(By.XPATH, '//*[@id="btnServicos"]/ul/li/a').click()


def acessar_guia_8(navegador):
    navegador.find_element(By.XPATH,
        '//*[@id="divTODOS_paginacao"]/span/a[8]').click()


def acessar_campo_nfe_nfce(navegador):
    navegador.find_element(By.XPATH, '//*[@id="divTODOS16"]/ul/li[4]/a').click()


def acesso_modulo_servicos(navegador):
    time.sleep(2)
    excecao_navegador(acessar_servicos, navegador)
    time.sleep(2)
    excecao_navegador(acessar_guia_8, navegador)
    time.sleep(2)
    excecao_navegador(acessar_campo_nfe_nfce, navegador)
    time.sleep(2)
    return navegador
