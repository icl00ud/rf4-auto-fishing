import os
import pyautogui
import time
from actions.subactions.check_fish_catch import catch_fish
from actions.subactions.fish_fight import fight_fish
from common.common_functions import is_hooked, is_ready_for_launch, is_fish_caught


def launch_bait():
    print("Launching the bait...")
    pyautogui.keyDown("shift")
    time.sleep(0.3)
    pyautogui.mouseDown(button="left")
    time.sleep(0.65)
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    time.sleep(2.3)


def pull_bait_spinning():
    secondsPulling = 0
    print("Pulling the bait...")
    pyautogui.mouseDown(button="left")
    while True:
        secondsPulling += 1
        print(f"Seconds pulling: {secondsPulling}")
        time.sleep(1)
        if is_ready_for_launch():
            break
        if is_hooked():
            break
        if is_fish_caught():
            break

    pyautogui.mouseUp(button="left")
    os.system("cls")

def pull_bait_twitching():
    secondsTwitching = 0
    print("Twitching...")
    while True:
        secondsTwitching += 1
        print(f"Seconds Twitching: {secondsTwitching}")
        pyautogui.mouseDown(button="left")
        pyautogui.click(button="right")
        pyautogui.mouseUp(button="left")
        if is_ready_for_launch():
            break
        if is_hooked():
            break
        if is_fish_caught():
            break
        os.system("cls")
