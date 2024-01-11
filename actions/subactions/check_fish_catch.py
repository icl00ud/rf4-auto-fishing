import time
import pyautogui

from common.common_functions import capture_trophy_screenshot


def catch_fish():
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")
    capture_trophy_screenshot()
    pyautogui.press("space")
