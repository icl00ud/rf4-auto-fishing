import keyboard
import threading
from actions.cast import start_spinning

def on_press(key):
    global is_running
    if key.name == 'F3':
        if not is_running:
            print("Bot running")
            is_running = True
            threading.Thread(target=start_spinning).start()
            

def monitor_keyboard():
    global is_running
    is_running = False

    keyboard.on_press_key('F3', on_press)
    keyboard.on_press_key('F8', on_press)

    while True:
        if keyboard.is_pressed('F8'):
            print("Bot stopped")
            is_running = False
            break

if __name__ == '__main__':
    monitor_keyboard()