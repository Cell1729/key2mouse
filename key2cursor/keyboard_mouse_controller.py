# キーボードの入力に対してマウスカーソルを動かす
import keyboard
import pyautogui
from key2cursor.lib.json_manager import load_json

JSON_PATH = r'key2cursor/key_config.json'

class KeyboardMouseController:
    def __init__(self):
        self.json_data = load_json(JSON_PATH)
        # mouse move settings
        self.mouse_speed = self.json_data["options"]["cursorSpeed"]
        self.scroll_speed = self.json_data["options"]["scrollSpeed"]
        self.mouse_mode = self.json_data["mouseMove"]["mouseMode"]
        self.move_up = self.json_data["mouseMove"]["moveUp"]
        self.move_down = self.json_data["mouseMove"]["moveDown"]
        self.move_left = self.json_data["mouseMove"]["moveLeft"]
        self.move_right = self.json_data["mouseMove"]["moveRight"]
        # click events
        self.left_click_key = self.json_data["clickEvents"]["leftClick"]
        self.right_click_key = self.json_data["clickEvents"]["rightClick"]
        self.scroll_up_key = self.json_data["clickEvents"]["scrollUp"]
        self.scroll_down_key = self.json_data["clickEvents"]["scrollDown"]

    def keyboard_observer(self):
        # マウスの移動
        keyboard.add_hotkey(f"{self.move_up}+{self.mouse_mode}", self.on_up)
        keyboard.add_hotkey(f"{self.move_down}+{self.mouse_mode}", self.on_down)
        keyboard.add_hotkey(f"{self.move_left}+{self.mouse_mode}", self.on_left)
        keyboard.add_hotkey(f"{self.move_right}+{self.mouse_mode}", self.on_right)
        # マウスのクリック
        keyboard.add_hotkey(f"{self.left_click_key}+{self.mouse_mode}", self.left_click)
        keyboard.add_hotkey(f"{self.right_click_key}+{self.mouse_mode}", self.right_click)
        # マウスのスクロール
        keyboard.add_hotkey(f"{self.scroll_up_key}+{self.mouse_mode}", self.scroll_up)
        keyboard.add_hotkey(f"{self.scroll_down_key}+{self.mouse_mode}", self.scroll_down)
        keyboard.wait()

    def on_up(self):
        now_cursor = pyautogui.position()
        pyautogui.moveTo(now_cursor.x, now_cursor.y - self.mouse_speed)

    def on_down(self):
        now_cursor = pyautogui.position()
        pyautogui.moveTo(now_cursor.x, now_cursor.y + self.mouse_speed)

    def on_left(self):
        now_cursor = pyautogui.position()
        pyautogui.moveTo(now_cursor.x - self.mouse_speed, now_cursor.y)

    def on_right(self):
        now_cursor = pyautogui.position()
        pyautogui.moveTo(now_cursor.x + self.mouse_speed, now_cursor.y)

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def scroll_up(self):
        pyautogui.scroll(self.scroll_speed)

    def scroll_down(self):
        pyautogui.scroll(self.scroll_speed * -1)
