import datetime
import os
import pyautogui


def find_image_on_screen(image_path):
    try:
        image_location = pyautogui.locateOnScreen(image_path, confidence=0.8, grayscale=True)
        if image_location:
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        return False


def is_fish_caught():
    image_path = "./screenshots/fish-catched-2.png"
    image_path2 = "./screenshots/fish-catched-3.png"
    image_path3 = "./screenshots/fish-catched-3.png"
    if (
        find_image_on_screen(image_path)
        or find_image_on_screen(image_path2)
        or find_image_on_screen(image_path3)
    ):
        print("Fish captured!")
        return True
    else:
        return False


def is_ready_for_launch():
    image_path_1 = './screenshots/ready-for-launch-1.png'
    image_path_2 = './screenshots/ready-for-launch-2.png'
    image_path_2 = './screenshots/ready-for-launch-3.png'
    image_path_3 = './screenshots/ready-for-launch-4.png'
    if (
        find_image_on_screen(image_path_1) 
        or find_image_on_screen(image_path_2) 
        or find_image_on_screen(image_path_2) 
        or find_image_on_screen(image_path_3)
    ):
        return True
    else:
        return False


def is_hooked():
    image_path = "./screenshots/fish-in-line.png"
    if find_image_on_screen(image_path):
        print("Fish catched!")
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


def capture_screenshot():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

    destination_folder = os.path.expanduser("~/OneDrive/Russian Fishing 4 - Images")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    screenshot = pyautogui.screenshot()

    file_name = f"screenshot_{timestamp}.png"

    file_path = os.path.join(destination_folder, file_name)
    screenshot.save(file_path)

    print(f"Screenshot saved at: {file_path}")
