from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

def type_text_slowly(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    time.sleep(10)

    for char in content:
        if char == "\n":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
        elif char == "}":
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        else:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.2)

file_path = "texto.txt"
type_text_slowly(file_path)

