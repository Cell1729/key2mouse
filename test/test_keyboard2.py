import keyboard
import pyautogui

MOUSE_MODE = 'n'
MOUSE_SPEED = 25

MOVE_UP = 'e'
MOVE_DOWN = 'd'
MOVE_LEFT = 's'
MOVE_RIGHT = 'f'


def on_up():
    print("上に移動")
    now_cursor = pyautogui.position()
    pyautogui.moveTo(now_cursor.x, now_cursor.y - MOUSE_SPEED)

def on_down():
    print("下に移動")
    now_cursor = pyautogui.position()
    pyautogui.moveTo(now_cursor.x, now_cursor.y + MOUSE_SPEED)

def on_left():
    print("左に移動")
    now_cursor = pyautogui.position()
    pyautogui.moveTo(now_cursor.x - MOUSE_SPEED, now_cursor.y)

def on_right():
    print("右に移動")
    now_cursor = pyautogui.position()
    pyautogui.moveTo(now_cursor.x + MOUSE_SPEED, now_cursor.y)

keyboard.add_hotkey(f"{MOVE_UP}+{MOUSE_MODE}", on_up)
keyboard.add_hotkey(f"{MOVE_DOWN}+{MOUSE_MODE}", on_down)
keyboard.add_hotkey(f"{MOVE_LEFT}+{MOUSE_MODE}", on_left)
keyboard.add_hotkey(f"{MOVE_RIGHT}+{MOUSE_MODE}", on_right)
keyboard.wait()
