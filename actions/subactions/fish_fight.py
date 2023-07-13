import time
import pyautogui
from actions.subactions.check_fish_catch import catch_fish

from common.common_functions import is_fish_caught, move_mouse


def fight_fish():
    print("Puxando peixe...")
    time.sleep(0.1)
    move_mouse("up", 1500)
    pyautogui.mouseDown(button="left")
    pyautogui.mouseDown(button="right")
    pyautogui.keyDown("shift")
    if is_fish_caught():
        catch_fish()
    else:
        move_mouse("down", 1500)
        pyautogui.mouseUp(button="left")
        pyautogui.mouseUp(button="right")
        pyautogui.keyUp("shift")
