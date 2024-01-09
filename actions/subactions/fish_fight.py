import pyautogui
from actions.subactions.check_fish_catch import catch_fish

from common.common_functions import is_fish_caught


def fight_fish():
    if is_fish_caught():
            catch_fish()
    else:
        print("Fighting with the fish...")
        pyautogui.mouseDown(button="left")
        pyautogui.mouseDown(button="right")
        pyautogui.keyDown("shift")
