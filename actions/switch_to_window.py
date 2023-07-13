import time
import pygetwindow as gw

def switch_to_rf4_window():
    target_process = 'Russian Fishing 4'

    rf4_window = gw.getWindowsWithTitle(target_process)
    
    if rf4_window:
        rf4_window[0].activate()
        print("Janela do jogo encontrada e ativada.")
    else:
        print('Janela não encontrada.')