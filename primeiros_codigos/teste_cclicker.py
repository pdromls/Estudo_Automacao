# Este código abre o navegador, acessa o jogo Cookie Clicker e automatiza cliques para jogar.
import pyautogui as pag
import time
import keyboard

# pag.PAUSE = 0.3

pag.press('win')
time.sleep(0.3)
pag.write('chrome')
time.sleep(0.3)
pag.press('enter')
time.sleep(2)
pag.click(x=686, y=669) #selecionando meu usuário do chrome
time.sleep(0.3)
pag.click(x=586, y=64) #clicando na barra de pesquisa
time.sleep(0.3)
pag.press('backspace')
time.sleep(0.3)

pag.write('https://orteil.dashnet.org/cookieclicker/')
time.sleep(0.3)
pag.press('enter')
time.sleep(5)

num_clicks = 10000  # Número de cliques que você quer fazer
clicks = 0

for clicks in range(num_clicks):
    if keyboard.is_pressed('esc'):  # Para o loop se 'esc' for pressionado
        print("Parando script...")
        break
    if clicks % 100 == 0: # A cada 100 cliques, tenta comprar um upgrade
        pag.click(x=1631, y=555)
        time.sleep(0.3)
        pag.moveTo(x=1686, y=800) # Move o cursor para o terceiro upgrade
        time.sleep(0.3)
        pag.click(x=1686, y=800) # Coordenadas do terceiro upgrade
        time.sleep(0.3)
        pag.click(x=1686, y=730) # Coordenadas do segundo upgrade 
        time.sleep(0.3)
        pag.click(x=1686, y=659) # Coordenadas do primeiro upgrade 
        time.sleep(0.3)
    pag.doubleClick(x=276, y=496) # Coordenadas do cookie
    clicks += 1
    # time.sleep(0.01)  # Pequena pausa entre os cliques 