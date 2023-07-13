import os
import pyautogui
import time
from actions.subactions.fish_fight import fight_fish
from common.common_functions import is_hooked, is_ready_for_launch


def launch_bait():
    print("Lançando a isca...")
    pyautogui.mouseDown(button="left")
    pyautogui.keyDown("shift")
    time.sleep(0.5)
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    time.sleep(2.3)


def pull_bait():
    secondsPulling = 0
    print("Puxando a isca...")
    pyautogui.mouseDown(button="left")
    while True:
        secondsPulling += 1
        print(f"Segundos puxando: {secondsPulling}")
        time.sleep(1)  # Espera 1 segundo

        if is_ready_for_launch():
            break

        if is_hooked():
            pyautogui.mouseUp(button="left")
            fight_fish()
            break

    pyautogui.mouseUp(button="left")
    os.system("cls")
