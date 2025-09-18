# Passo 1: Entrar no Excel e abrir a planilha
# Passo 2: Selecionar corretamente a célula
# Passo 3: Inserir os dados nas células
# Passo 4: Salvar a planilha

import pyautogui as pag
import time
import keyboard

pag.PAUSE = 0.5

pag.press('win')
pag.write('excel')
pag.press('enter')
time.sleep(5)
pag.press('tab', presses=2, interval=0.5)
pag.write('Planilha_Cadastros')
pag.press('enter')
time.sleep(2)

clientes = [
    # {"categoria": 1, "nome": "Joao", "servico": "Consultoria", "data": "18/09/2025", "preco": 100}, já cadastrados
    # {"categoria": 2, "nome": "Maria", "servico": "Treinamento", "data": "19/09/2025", "preco": 200},
    # {"categoria": 3, "nome": "Pedro", "servico": "Desenvolvimento", "data": "20/09/2025", "preco": 300},
    # {"categoria": 1, "nome": "Ana", "servico": "Consultoria", "data": "21/09/2025", "preco": 150},
    # {"categoria": 2, "nome": "Lucas", "servico": "Treinamento", "data": "22/09/2025", "preco": 250},
    # {"categoria": 1, "nome": "Antonio", "servico": "Consultoria", "data": "18/09/2025", "preco": 100},
    # {"categoria": 2, "nome": "Marcia", "servico": "Treinamento", "data": "19/09/2025", "preco": 200},
    # {"categoria": 3, "nome": "Pedro Henrique", "servico": "Desenvolvimento", "data": "20/09/2025", "preco": 300},
    # {"categoria": 1, "nome": "Ana Clara", "servico": "Consultoria", "data": "21/09/2025", "preco": 150},
    # {"categoria": 2, "nome": "Isis", "servico": "Treinamento", "data": "22/09/2025", "preco": 250},
    {"categoria": 1, "nome": "Matheus", "servico": "Consultoria", "data": "18/09/2025", "preco": 100},
    {"categoria": 2, "nome": "Manuela", "servico": "Treinamento", "data": "19/09/2025", "preco": 200},
    {"categoria": 3, "nome": "Luis Felipe", "servico": "Desenvolvimento", "data": "20/09/2025", "preco": 300},
    {"categoria": 1, "nome": "Camille", "servico": "Consultoria", "data": "21/09/2025", "preco": 150},
    {"categoria": 2, "nome": "Bruno", "servico": "Treinamento", "data": "22/09/2025", "preco": 250},
]

time.sleep(2) # Espera o Excel abrir

for cliente in clientes:
    if keyboard.is_pressed('esc'):  # Para o loop se 'esc' for pressionado
        break

    if cliente["categoria"] == 1:
        pag.click(x=156, y=990) # Clica na planilha Categoria1
        for _ in range(3): # Vai até a célula A1
            pag.hotkey('ctrl', 'up')
        pag.hotkey('ctrl', 'left')

    elif cliente["categoria"] == 2:
        pag.click(x=262, y=994) # Clica na planilha Categoria2
        for _ in range(3): # Vai até a célula A1
            pag.hotkey('ctrl', 'up')
        pag.hotkey('ctrl', 'left')

    elif cliente["categoria"] == 3:
        pag.click(x=354, y=990) # Clica na planilha Categoria3
        for _ in range(3): # Vai até a célula A1
            pag.hotkey('ctrl', 'up')
        pag.hotkey('ctrl', 'left')

    pag.press('tab', presses=2, interval=0.5)
    for _ in range(3):
        pag.hotkey('ctrl', 'down')
    pag.hotkey('ctrl', 'up')
    pag.press('down')
    pag.write(cliente["nome"])
    pag.press('tab')
    pag.write(cliente["servico"])
    pag.press('tab')
    pag.write(cliente["data"])
    pag.press('tab')
    pag.write(str(cliente["preco"]))

pag.press('enter')
pag.hotkey('ctrl', 'b') # Salva a planilha

# Esse código apenas adiciona os novos clientes, sem verificar se já existem. O próximo passo será implementar essa verificação.