from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import *
import time
from excecoes.excecao_navegador import excecao_navegador


def clicar_area_informacional(navegador):
    navegador.find_element(By.XPATH,
        '//*[@id="areaInformacional"]/div[2]/input').click()


def fechar_informacao(navegador):
    navegador.find_element(By.XPATH, '//*[@id="cboxClose"]').click()


def conectar():

    with open('R:\Compartilhado\Fiscal\lista_clientes_sefaz\credenciais.txt', 'r') as arquivo:
        credenciais = arquivo.readlines()

    LINK = credenciais[0].replace('\n', '')
    CHAVE_API = credenciais[1].replace('\n', '')
    CPF = credenciais[2].replace('\n', '')
    SENHA = credenciais[3].replace('\n', '')
    

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": "c:\sefaz",
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True,
        "download.directory_upgrade": True,

        "plugins.always_open_pdf_externally": True,
        "selectedDestinationId": "Salvar como PDF"
    }

    options.add_experimental_option("prefs", prefs)
    navegador = webdriver.Chrome(
        chrome_options=options, service=Service(ChromeDriverManager().install()))

    # navegador = webdriver.Chrome(
    #     service=Service(ChromeDriverManager().install()))

    navegador.get(LINK)
    navegador.maximize_window()

    navegador.find_element(By.XPATH,
        '//*[@id="LoginId"]').send_keys(CPF)

    navegador.find_element(By.XPATH, 
        '//*[@id="senha_ecac"]').send_keys(SENHA)

    chave_captcha = navegador.find_element(
        By.CLASS_NAME, 'g-recaptcha').get_attribute('data-sitekey')

    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)  # printando status captcha '1'
    solver.set_key(CHAVE_API)
    solver.set_website_url(LINK)
    solver.set_website_key(chave_captcha)

    resposta = solver.solve_and_return_solution()

    if resposta != 0:
        print(resposta)
        # preencher o campo do token do captcha
        # g-recaptcha-response
        navegador.execute_script(
            f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
        navegador.find_element(By.ID, 'btnEntrar').click()
    else:
        print(solver.err_string)

    excecao_navegador(clicar_area_informacional, navegador)
    excecao_navegador(fechar_informacao, navegador)

    return navegador


if __name__ == '__main__':
    conectar()
