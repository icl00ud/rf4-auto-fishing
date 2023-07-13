import time
import pyautogui

from common.common_functions import move_mouse


def catch_fish():
    move_mouse("down", 1500)
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")
    time.sleep(0.1)
    pyautogui.press("space")
    time.sleep(0.1)
    time.sleep(0.1)