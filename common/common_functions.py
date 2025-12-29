import datetime
import os

import pyautogui

import globals


def release_all_keys():
    pyautogui.keyUp("shift")
    pyautogui.mouseUp(button="left")
    pyautogui.mouseUp(button="right")


def find_image_on_screen(image_path):
    try:
        image_location = pyautogui.locateOnScreen(
            image_path, confidence=0.8, region=globals.region
        )
        return image_location is not None
    except pyautogui.ImageNotFoundException:
        return False


def is_fish_caught():
    image_path_3 = "./screenshots/fish-catched-3.png"
    image_path_4 = "./screenshots/fish-catched-4.png"
    result = find_image_on_screen(image_path_3) or find_image_on_screen(image_path_4)
    if result:
        print("Fish captured!")
    return result


def is_ready_for_launch():
    image_path_1 = "./screenshots/ready-for-launch-1.png"
    image_path_2 = "./screenshots/ready-for-launch-2.png"
    return find_image_on_screen(image_path_1) or find_image_on_screen(image_path_2)


def is_hooked():
    image_path = "./screenshots/fish-in-line.png"
    result = find_image_on_screen(image_path)
    if result:
        print("Fish in line!")
    return result


def is_hungry():
    hungry_image_path = "./screenshots/hungry.png"
    return find_image_on_screen(hungry_image_path)


def eat():
    bread_image_path = "./screenshots/bread.png"
    pyautogui.keyDown("T")

    if find_image_on_screen(bread_image_path):
        image_position = pyautogui.locateOnScreen(bread_image_path, confidence=0.9)
        if image_position:
            image_center = pyautogui.center(image_position)
            pyautogui.moveTo(image_center)
            pyautogui.click(button="left")
    else:
        print("Could not find the bread")

    pyautogui.keyUp("T")


def capture_trophy_screenshot():
    if find_image_on_screen("./screenshots/trophy.png"):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

        destination_folder = os.path.expanduser("~/Downloads/Russian Fishing 4")

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        file_name = f"screenshot_{timestamp}.png"
        file_path = os.path.join(destination_folder, file_name)

        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)
