import pyautogui

from common.common_functions import capture_trophy_screenshot


def catch_fish():
    # --------- Keys reset
    all_keys = pyautogui.KEYBOARD_KEYS
    for key in all_keys:
        pyautogui.keyUp(key)
    # ---------
    
    capture_trophy_screenshot()
    pyautogui.press("space")
