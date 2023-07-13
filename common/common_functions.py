import pyautogui


def find_image_on_screen(image_path):
    image_location = pyautogui.locateOnScreen(image_path, confidence=0.9)
    if image_location:
        return True
    else:
        return False


def move_mouse(direction, pixels):
    current_x, current_y = pyautogui.position()
    if direction == "up":
        new_y = current_y - pixels
        pyautogui.moveTo(current_x, new_y, duration=1)
    elif direction == "down":
        new_y = current_y + pixels
        pyautogui.moveTo(current_x, new_y, duration=1)
    else:
        raise ValueError("Direção inválida. Use 'up' ou 'down'.")


def is_fish_caught():
    image_path = "./screenshots/fish-catched.png"
    image_path2 = "./screenshots/fish-catched-2.png"
    if find_image_on_screen(image_path) or find_image_on_screen(image_path2):
        print("Peixe capturado!")
        return True
    else:
        return False


def is_ready_for_launch():
    image_path = "./screenshots/ready-for-launch.png"
    if find_image_on_screen(image_path):
        return True
    else:
        return False


def is_hooked():
    image_path = "./screenshots/fish-in-line.png"
    if find_image_on_screen(image_path):
        print("Peixe fisgado!")
        return True
    else:
        return False
