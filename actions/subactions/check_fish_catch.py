import time
import pyautogui


def catch_fish():
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")
    time.sleep(0.1)
    pyautogui.press("space")
    time.sleep(0.1)
