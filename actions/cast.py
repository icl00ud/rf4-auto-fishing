import pyautogui
import pygetwindow as gw
import time
import os

def switch_to_rf4_window():
    target_process = 'Russian Fishing 4'

    rf4_window = gw.getWindowsWithTitle(target_process)
    
    if rf4_window:
        rf4_window[0].activate()
        print("Janela do jogo encontrada e ativada.")
    else:
        print('Processo rf4_x64.exe não encontrado.')
    os.system('cls') or None
    time.sleep(0.5)

def cast_bait():  
    os.system('cls') or None
    print("Executando ação de jogar a isca...")
    pyautogui.mouseDown(button='left')
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    pyautogui.keyUp('shift')
    pyautogui.mouseUp(button='left')
    time.sleep(2.3)

def pull_bait():
    os.system('cls') or None
    print("Executando ação de puxar a isca...")
    pyautogui.mouseDown(button='left')
    time.sleep(8)
    pyautogui.mouseUp(button='left')

def find_image_on_screen(image_path):
    image_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    return image_location is not None

def start_spinning():
    while True:
        print("Iniciando o bot...")
        switch_to_rf4_window()
        
        image_path = './screenshots/ready-for-launch.png'
        if find_image_on_screen(image_path):
            print("Equipamento pronto para lançamento.")
            cast_bait()
            pull_bait()
            os.system('cls') or None
            print("Rotina executada com sucesso!")
        else:
            print("Equipamento não está pronto para lançamento.")
        time.sleep(1)