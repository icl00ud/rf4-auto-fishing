import pyautogui

from common.common_functions import capture_trophy_screenshot, release_all_keys


def catch_fish():
    release_all_keys()
    capture_trophy_screenshot()
    pyautogui.press("space")
