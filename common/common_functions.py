import pyautogui


def find_image_on_screen(image_path):
    image_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if image_location:
        return True
    else:
        return False
