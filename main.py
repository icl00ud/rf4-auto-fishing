import os

import keyboard

import globals
from actions.spinning import start_spinning
from actions.twitching import start_twitching


def on_press(event):
    if event.name == "f3":
        if not globals.is_running:
            globals.is_running = True
            os.system("cls")
            start_spinning()
    elif event.name == "f4":
        if not globals.is_running:
            globals.is_running = True
            os.system("cls")
            start_twitching()
    elif event.name == "f8":
        if globals.is_running:
            globals.is_running = False
            print("Bot stopped")


def monitor_keyboard():
    globals.is_running = False
    keyboard.on_press(on_press)

    while True:
        if keyboard.is_pressed("f8"):
            break


if __name__ == "__main__":
    os.system("cls")
    print("F3 - Spinning")
    print("F4 - Twitching")
    print("F8 - Break the bot")
    monitor_keyboard()
