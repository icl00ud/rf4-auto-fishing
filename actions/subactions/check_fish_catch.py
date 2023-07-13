import time
import pyautogui

from common.common_functions import capture_screenshot


def catch_fish():
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")
    capture_screenshot()
    time.sleep(0.1)
    pyautogui.press("space")
    time.sleep(0.1)
