import time
import pyautogui

from actions.subactions.check_fish_catch import is_fish_caught, catch_fish
from common.common_functions import find_image_on_screen


def is_hooked():
    image_path = "./screenshots/fish-in-line.png"
    if find_image_on_screen(image_path):
        print("Peixe fisgado!")
        return True
    else:
        return False


def fight_fish():
    print("Puxando peixe...")
    time.sleep(0.1)
    pyautogui.mouseDown(button="left")
    pyautogui.mouseDown(button="right")
    pyautogui.keyDown("shift")
    pyautogui.move(0, -200)
    if is_fish_caught():
        catch_fish()
