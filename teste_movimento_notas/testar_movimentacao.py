import pyautogui
import time


def tem_movimento():
    # vair retornar o box(......)
    time.sleep(1)
    return pyautogui.locateOnScreen('msg_nao_ha_canceladas.png')
