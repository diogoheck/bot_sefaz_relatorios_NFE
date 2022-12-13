import pyautogui


def salvar_relatorio_janela_1():
    return pyautogui.locateOnScreen('botao_salvar_1.png')


def salvar_relatorio_janela_2():
    return pyautogui.locateOnScreen('botao_salvar_2.png') or pyautogui.locateOnScreen('botao_salvar_2.1.png')
