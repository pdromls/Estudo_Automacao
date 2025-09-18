# Este código abre o navegador, acessa um vídeo do YouTube e posta um comentário.
import pyautogui as pag
import time

pag.PAUSE = 0.5

pag.press('win')
pag.write('chrome')
pag.press('enter')
time.sleep(2)
pag.click(x=686, y=669) #selecionando meu usuário do chrome
pag.click(x=586, y=64) #clicando na barra de pesquisa
pag.press('backspace')


pag.write('https://youtu.be/DGDSYSczbYc')
pag.press('enter')
time.sleep(5)
pag.moveTo(x=55, y=436)
pag.scroll(-500)
time.sleep(1)
pag.click(x=496, y=749) #clicando na barra de comentários
pag.write('Que belo clutch!')
pag.press('tab', presses=3)
pag.press('enter')
time.sleep(2)

pag.scroll(500)