# Jsonファイルに設定を保存するクラス
import json
from key2cursor.lib.json_manager import load_json

JSON_PATH = r'key2cursor/key_config.json'

class ConfigManager:
    def __init__(self):
        self.json_data = load_json(JSON_PATH)

    def save_move_up(self, value):
        self.json_data['mouseMove']['moveUp'] = value
        self.save_json()

    def save_move_down(self, value):
        self.json_data['mouseMove']['moveDown'] = value
        self.save_json()

    def save_move_left(self, value):
        self.json_data['mouseMove']['moveLeft'] = value
        self.save_json()

    def save_move_right(self, value):
        self.json_data['mouseMove']['moveRight'] = value
        self.save_json()

    def save_mouse_mode(self, value):
        self.json_data['mouseMove']['mouseMode'] = value
        self.save_json()

    def save_click_left(self, value):
        self.json_data['clickEvents']['clickLeft'] = value
        self.save_json()
    def save_click_right(self, value):
        self.json_data['clickEvents']['clickRight'] = value
        self.save_json()

    def save_scroll_up(self, value):
        self.json_data['scrollEvents']['scrollUp'] = value
        self.save_json()

    def save_scroll_down(self, value):
        self.json_data['scrollEvents']['scrollDown'] = value
        self.save_json()

    def save_options(self, cursor_speed, scroll_speed):
        self.json_data['options']['cursorSpeed'] = cursor_speed
        self.json_data['options']['scrollSpeed'] = scroll_speed
        self.save_json()

    def save_json(self):
        with open(JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.json_data, f, ensure_ascii=False, indent=2)