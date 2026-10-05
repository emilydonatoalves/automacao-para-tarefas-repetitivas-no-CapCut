import pyautogui
import time
import pyperclip

    # 1º Passo: editar a proporção

pyautogui.PAUSE = 0.3

pyautogui.click(x=1033, y=467)
pyautogui.click(x=1088, y=681)

# 2º Passo: Arrastar template foto para a linha do tempo

pyautogui.click(x=63, y=237)
pyautogui.click(x=74, y=234)

pyautogui.moveTo(328, 354, duration=0.3)
time.sleep(0.5)

pyautogui.mouseDown()
time.sleep(0.5)

pyautogui.moveTo(185, 612, duration=1)

time.sleep(0.5)
pyautogui.mouseUp()

    # 3º Passo: Arrastar template efeito para a linha do tempo

pyautogui.moveTo(330, 242, duration=0.3)
time.sleep(0.5)

pyautogui.mouseDown()
time.sleep(0.5)

pyautogui.moveTo(182, 581, duration=1)

time.sleep(0.5)
pyautogui.mouseUp()

    # 4º Passo: Arrastar template texto para a linha do tempo

pyautogui.moveTo(331, 462, duration=0.3)
time.sleep(0.5)

pyautogui.mouseDown()
time.sleep(0.5)

pyautogui.moveTo(180, 581, duration=1)

time.sleep(0.5)
pyautogui.mouseUp()

    # 5º Passo: Arrastar template musica para a linha do tempo

pyautogui.moveTo(228, 462, duration=0.3)
time.sleep(0.5)

pyautogui.mouseDown()
time.sleep(0.5)

pyautogui.moveTo(183, 764, duration=1)

time.sleep(0.5)
pyautogui.mouseUp()

    # 6º Passo: Arrastar template rodapé para a linha do tempo

pyautogui.moveTo(198, 345, duration=0.3)
time.sleep(0.5)

pyautogui.mouseDown()
time.sleep(0.5)

pyautogui.moveTo(184, 570, duration=1)

time.sleep(0.5)
pyautogui.mouseUp()

    # 7º Passo: Passo: cortar templates

pyautogui.press('down')
pyautogui.click(x=1453, y=575)
pyautogui.click(x=269, y=632)
pyautogui.hotkey('option', 'shift', 'g')
time.sleep(0.5)
pyautogui.press('down')
pyautogui.hotkey('command', 'a')
pyautogui.click(x=278, y=519)
time.sleep(0.5)

   # 8º Passo: Passo: escrever o título
   # Biblioteca paperclip função copy para copiar e colar o titulo e não ficar sem acento

pyautogui.click(x=300, y=616)
pyautogui.click(x=1226, y=218)
pyautogui.hotkey('command', 'a')
time.sleep(0.5)
titulo = "Está tudo cada \nvez mais caro"
pyperclip.copy(titulo)
pyautogui.hotkey("command", "v") 

time.sleep(0.5)

    # 9º Passo: Exportar

pyautogui.click(x=1418, y=52)
time.sleep(0.5)
pyautogui.press('return')