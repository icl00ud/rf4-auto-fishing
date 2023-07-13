import time
import pyautogui
from actions.subactions.check_fish_catch import catch_fish

from common.common_functions import is_fish_caught


def fight_fish():
    if is_fish_caught():
            catch_fish()
    else:
        pyautogui.mouseUp(button="left")
        pyautogui.mouseUp(button="right")
        pyautogui.keyUp("shift")
    print("Puxando peixe...")
    time.sleep(0.1)
    pyautogui.mouseDown(button="left")
    pyautogui.mouseDown(button="right")
    pyautogui.keyDown("shift")
    
