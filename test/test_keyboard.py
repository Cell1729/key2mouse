import keyboard
import pyautogui

MOUSE_MODE = 'n'
MOUSE_SPEED = 50

MOVE_UP = 'e'
MOVE_DOWN = 'd'
MOVE_LEFT = 's'
MOVE_RIGHT = 'f'

while True:
    now_cursor = pyautogui.position()
    if keyboard.is_pressed(MOVE_UP) and keyboard.is_pressed(MOUSE_MODE):
        pyautogui.moveTo(now_cursor.x, now_cursor.y - MOUSE_SPEED)
    elif keyboard.is_pressed(MOVE_DOWN) and keyboard.is_pressed(MOUSE_MODE):
        pyautogui.moveTo(now_cursor.x, now_cursor.y + MOUSE_SPEED)
    elif keyboard.is_pressed(MOVE_LEFT) and keyboard.is_pressed(MOUSE_MODE):
        pyautogui.moveTo(now_cursor.x - MOUSE_SPEED, now_cursor.y)
    elif keyboard.is_pressed(MOVE_RIGHT) and keyboard.is_pressed(MOUSE_MODE):
        pyautogui.moveTo(now_cursor.x + MOUSE_SPEED, now_cursor.y)
    elif keyboard.is_pressed('q'):
        break