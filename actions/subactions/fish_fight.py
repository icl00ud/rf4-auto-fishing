import pyautogui

from common.common_functions import is_fish_caught


def fight_fish():
    if not is_fish_caught():
        print("Fighting with the fish...")
        pyautogui.mouseDown(button="left")
        pyautogui.mouseDown(button="right")
        pyautogui.keyDown("shift")
