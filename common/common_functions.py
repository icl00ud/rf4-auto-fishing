import datetime
import os
import pyautogui
import globals


def find_image_on_screen(image_path):
    try:
        image_location = pyautogui.locateOnScreen(image_path, confidence=0.8, region=globals.region)
        if image_location:
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False


def is_fish_caught():
    image_path_3 = "./screenshots/fish-catched-3.png"
    image_path_4 = "./screenshots/fish-catched-4.png"
    if find_image_on_screen(image_path_3) or find_image_on_screen(image_path_4):
        print("Fish captured!")
        return True
    else:
        return False


def is_ready_for_launch():
    image_path_1 = './screenshots/ready-for-launch-1.png'
    image_path_2 = './screenshots/ready-for-launch-2.png'
    if find_image_on_screen(image_path_1) or find_image_on_screen(image_path_2):
        return True
    else:
        return False


def is_hooked():
    image_path = "./screenshots/fish-in-line.png"
    if find_image_on_screen(image_path):
        print("Fish in line!")
        return True
    else:
        return False


def is_hungry():
    hungry_image_path = "./screenshots/hungry.png"
    if find_image_on_screen(hungry_image_path):
        return True
    else:
        return False


def eat():
    bread_image_path = "./screenshots/bread.png"
    pyautogui.keyDown("T")
    
    if find_image_on_screen(bread_image_path):
        image_position = pyautogui.locateOnScreen(bread_image_path, confidence=0.9)
        if image_position:
            image_center = pyautogui.center(image_position)
            pyautogui.moveTo(image_center)
            pyautogui.mouseDown(button="left")
            pyautogui.mouseUp(button="left")
        pyautogui.keyUp("T")
    else:
        pyautogui.keyUp("T")
        print("Could not found the bread")


def capture_trophy_screenshot():
    if find_image_on_screen('./screenshots/trophy.png'):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

        destination_folder = os.path.expanduser("~/Downloads/Russian Fishing 4")

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        file_name = f"screenshot_{timestamp}.png"
        file_path = os.path.join(destination_folder, file_name)

        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)