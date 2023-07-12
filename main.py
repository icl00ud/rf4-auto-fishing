import keyboard

from actions.spinning import start_spinning


def on_press(event):
    global is_running
    
    if event.name == "f3":
        if not is_running:
            is_running = True
            start_spinning()
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
    print("Pressione F3 para iniciar e F8 para parar o bot")
    monitor_keyboard()
