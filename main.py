import keyboard

from actions.spinning import start_spinning
from actions.twitching import start_twitching


def on_press(event):
    global is_running

    if event.name == "f3":
        if not is_running:
            is_running = True
            start_spinning()
    elif event.name == "f4":
        if not is_running:
            is_running = True
            start_twitching()
    elif event.name == "f8":
        if is_running:
            print("Bot stopped")


def monitor_keyboard():
    global is_running
    is_running = False
    keyboard.on_press(on_press)

    while True:
        if keyboard.is_pressed("f8"):
            break


if __name__ == "__main__":
    print("F3 - Spinning")
    print("F4 - Twitching")
    print("F8 - Break the bot")
    monitor_keyboard()
