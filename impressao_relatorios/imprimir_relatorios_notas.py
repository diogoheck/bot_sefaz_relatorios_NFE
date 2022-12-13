from classe_acessos import Path
from janelas_salvar.janelas_salvar_relatorios import salvar_relatorio_janela_1, salvar_relatorio_janela_2
from excecoes.excecao_janelas import excecao_telas
import pyautogui
import time
from selenium.webdriver.common.by import By

LOCAL_SALVAR = r'C:\SEFAZ\RELATORIO_NOTAS'


def salvar_relatorio_nf(nome, indicador, competencia, pagina):
    if indicador == '1':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS SAIDAS {nome} {competencia}'
    elif indicador == '2':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS SAIDAS CANCELADAS {nome} {competencia} - PAG{pagina}'
    elif indicador == '3':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS ENTRADAS {nome} {competencia}'
    elif indicador == '4':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS EMISSAO PROPRIA {nome} {competencia}'
    elif indicador == '5':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS EMISSAO PROPRIA CANCELADAS {nome} {competencia} - PAG{pagina}'
    elif indicador == '6':
        novo_cliente = f'{LOCAL_SALVAR}\RELATORIO NOTAS EMISSAO TERCEIROS {nome} {competencia}'

    pyautogui.write(novo_cliente)


def print_relatorio_nf(navegador, nome, indicador, competencia):
    # navegador.find_element_by_xpath(Path.BOTAO_IMPRIMIR).click()
    # time.sleep(1)
    print('*' * 50)
    print(nome)
    print('*' * 50)
    pagina = 1
    # Rolar até o fim da página
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    botao_proximo = None
    while(True):
        pyautogui.hotkey('ctrl', 'p')
        excecao_telas(salvar_relatorio_janela_1)
        pyautogui.press('enter')
        excecao_telas(salvar_relatorio_janela_2)
        salvar_relatorio_nf(nome, indicador, competencia, pagina)
        pyautogui.press('enter')
        # pyautogui.hotkey('alt', 'f4')
        time.sleep(2)
        try:
            botao_proximo = navegador.find_element(
                By.XPATH, '//*[@id="conteudoResultExt"]/div[2]/a[3]')
            if botao_proximo is not None:
                botao_proximo.click()
                pagina += 1
                time.sleep(2)
        except:
            
            time.sleep(2)
            return navegador



        
            
