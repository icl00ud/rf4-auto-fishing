import time
import pyautogui

from common.common_functions import find_image_on_screen
from actions.subactions.cast import is_ready_for_launch, launch_bait, pull_bait


def is_fish_caught():
    image_path = "./screenshots/fish-catched.png"
    image_path2 = "./screenshots/fish-catched-2.png"
    if find_image_on_screen(image_path) or find_image_on_screen(image_path2):
        print("Peixe capturado!")
        return True
    else:
        return False


def catch_fish():
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")
    time.sleep(0.1)
    pyautogui.press("space")
    time.sleep(0.1)
    pyautogui.move(0, 200)
    time.sleep(0.1)
    if is_ready_for_launch():
        launch_bait()
        pull_bait()
