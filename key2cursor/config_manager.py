# Jsonファイルに設定を保存するクラス
import json
from key2cursor.lib.json_manager import load_json
import os

JSON_PATH = os.path.abspath(r'key2cursor/key_config.json')

class ConfigManager:
    SORT_KEYID = {
      "mouseMove": {
        "mouseMode": "mouse_mode",
        "moveUp": "up",
        "moveDown": "down",
        "moveLeft": "left",
        "moveRight": "right"
      },
      "clickEvents": {
        "leftClick": "left_click",
        "rightClick": "right_click",
        "scrollUp": "scroll_up",
        "scrollDown": "scroll_down"
      },
      "options": {
        "cursorSpeed": "cursor_speed",
        "scrollSpeed": "scroll_speed",
      }
    }

    def __init__(self):
        self.json_data = load_json(JSON_PATH)

    def save_keybind(self, key_id: str, value: str):
        for section, mapping in self.SORT_KEYID.items():
            for json_key, id_name in mapping.items():
                if id_name == key_id:
                    self.json_data[section][json_key] = value
                    self.save_json()
                    return

    def save_value(self, key_id: str, value: int):
        for section, mapping in self.SORT_KEYID.items():
            for json_key, id_name in mapping.items():
                if id_name == key_id:
                    self.json_data[section][json_key] = value
                    self.save_json()
                    return

    def save_json(self):
        with open(JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.json_data, f, ensure_ascii=False, indent=2)