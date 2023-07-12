import pyautogui
import time

from common.common_functions import find_image_on_screen


def is_ready_for_launch():
    image_path = "./screenshots/ready-for-launch.png"
    if find_image_on_screen(image_path):
        print("Equipamento pronto para lançamento.")
        return True
    else:
        print("Equipamento não está pronto para lançamento.")
        return False


def launch_bait():
    print("Lançando a isca...")
    pyautogui.mouseDown(button="left")
    pyautogui.keyDown("shift")
    time.sleep(0.5)
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    time.sleep(2.3)


def pull_bait():
    print("Puxando a isca...")
    pyautogui.mouseDown(button="left")
    time.sleep(33)
    pyautogui.mouseUp(button="left")
