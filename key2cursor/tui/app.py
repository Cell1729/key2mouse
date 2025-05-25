from textual import events
from textual.css.query import NoMatches
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Button, Label, ListItem, ListView, Static
from textual.containers import Vertical, Container
from .input_overlay import InputOverlay
from key2cursor.lib.json_manager import load_json
import os

JSON_PATH = os.path.abspath(r'key2cursor/key_config.json')

class TuiApp(App):
    TITLE = "Key2Cursor"
    BINDINGS = [
        Binding("q", "quit", "Quit the app"),
        Binding("e", "up", "Move Up"),
        Binding("d", "down", "Move Down"),
        Binding("s", "left", "Move Left"),
        Binding("f", "right", "Move Right"),
        Binding("w", "left_click", "Left Click"),
        Binding("r", "right_click", "Right Click"),
        Binding("t", "scroll_up", "Scroll Up"),
        Binding("g", "scroll_down", "Scroll Down"),
        Binding("1", "cursor_speed", "Cursor Speed"),
        Binding("2", "scroll_speed", "Scroll Speed"),
        Binding("3", "mouse_mode", "Mouse Mode"),
    ]
    NAME_MAP = {
        "e": "up",
        "d": "down",
        "s": "left",
        "f": "right",
        "w": "left_click",
        "r": "right_click",
        "t": "scroll_up",
        "g": "scroll_down",
        "1": "cursor_speed",
        "2": "scroll_speed",
        "3": "mouse_mode",
    }
    BINDINGS_LIST = {
        "up": "Move Up",
        "down": "Move Down",
        "left": "Move Left",
        "right": "Move Right",
        "left_click": "Left Click",
        "right_click": "Right Click",
        "scroll_up": "Scroll Up",
        "scroll_down": "Scroll Down",
        "cursor_speed": "Cursor Speed",
        "scroll_speed": "Scroll Speed",
        "mouse_mode": "Mouse Mode",
    }
    CSS_PATH = "style.tcss"
    VALUE_KEY = ["cursor_speed", "scroll_speed"]

    def __init__(self):
        super().__init__()
        self.key_list = None
        self.options = None
        self.json_data = load_json(JSON_PATH)


    def compose(self) ->ComposeResult:
        yield Header()
        yield Footer()
        # Key Bindings List
        self.key_list =  Container(
            ListView(
                ListItem(Label(f'Move Up - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveUp"]}">')),
                ListItem(Label(f'Move Down - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveDown"]}">')),
                ListItem(Label(f'Move Left - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveLeft"]}">')),
                ListItem(Label(f'Move Right - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveRight"]}">')),
                ListItem(Label(f'Left Click - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["leftClick"]}">')),
                ListItem(Label(f'Right Click - <{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["rightClick"]}">')),
                ListItem(Label(f'Scroll Up - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["scrollUp"]}">')),
                ListItem(Label(f'Scroll Down - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["scrollDown"]}">')),
                ListItem(Label(f"Cursor Speed - <{self.json_data["options"]["cursorSpeed"]}>")),
                ListItem(Label(f"Scroll Speed - <{self.json_data["options"]["scrollSpeed"]}>")),
            ),
            classes="bordered-list",
        )
        yield self.key_list
        # Mouse buttons
        yield Container(
            Static(""),
            Container(Button("Move Up", id="up"), classes="cell-center"),
            Static(""),
            Container(Button("Move Left", id="left"), classes="cell-center"),
            Container(
        Container(Button("Left Click", id="left_click"), classes="cell-center",id="left_click_container"),
                Container(
                    Button("Scroll Up", id="scroll_up"),
                    Button("Scroll Down", id="scroll_down"),
                    classes="cell-center", id="scroll_up_wheel"
                ),
                Container(Button("Right Click", id="right_click"),classes="cell-center",id="right_click_container"),
                classes="main-mouse-buttons",
            ),
            Container(Button("Move Right", id="right"), classes="cell-center"),
            Static(""),
            Container(Button("Move Down", id="down"), classes="cell-center"),
            Static(""),
            classes="bordered-buttons"
        )
        self.options =  Container(
            Vertical(
                Button("Cursor Speed", id="cursor_speed"),
                Button("Scroll Speed", id="scroll_speed"),
                Button("Mouse Mode", id="mouse_mode"),
                classes="option-buttons",
            ),
            classes="option-frame",
        )
        yield self.options

    def on_mount(self)->None:
        self.key_list.border_title = "Key Bindings"
        self.options.border_title = "Options"

    def on_key(self, event: events.Key) -> None:
        def press(button_id: str) -> None:
            """Press a button, should it exist."""
            try:
                self.query_one(f"#{button_id}", Button).press()
            except NoMatches:
                pass

        key = event.key
        button_id = self.NAME_MAP.get(key)
        if button_id is not None:
            press(self.NAME_MAP.get(key, key))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ok_btn":
            # Reload the JSON data and update the key list
            self.reload_json()
        elif event.button.id not in self.VALUE_KEY:
            # コールバックとしてreload_jsonを渡す
            self.push_screen(
                InputOverlay(self.BINDINGS_LIST[event.button.id], key_id=event.button.id, callback=self.reload_json))
        else:
            # カーソルやスクロールの速度を入力する画面を表示
            self.push_screen(InputOverlay(self.BINDINGS_LIST[event.button.id], key_id=event.button.id, int_only=True,
                                          callback=self.reload_json))

    def reload_json(self):
        """Reload the JSON data and update the key list."""
        self.json_data = load_json(JSON_PATH)
        list_view = self.key_list.query_one(ListView)
        list_view.clear()  # ListViewをクリア

        # 各ListItemを1つずつ追加
        list_view.append(ListItem(Label(
            f'Move Up - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveUp"]}">')))
        list_view.append(ListItem(Label(
            f'Move Down - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveDown"]}">')))
        list_view.append(ListItem(Label(
            f'Move Left - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveLeft"]}">')))
        list_view.append(ListItem(Label(
            f'Move Right - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["mouseMove"]["moveRight"]}">')))
        list_view.append(ListItem(Label(
            f'Left Click - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["leftClick"]}">')))
        list_view.append(ListItem(Label(
            f'Right Click - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["rightClick"]}">')))
        list_view.append(ListItem(Label(
            f'Scroll Up - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["scrollUp"]}">')))
        list_view.append(ListItem(Label(
            f'Scroll Down - <"{self.json_data["mouseMove"]["mouseMode"]}" + "{self.json_data["clickEvents"]["scrollDown"]}">')))
        list_view.append(ListItem(Label(f"Cursor Speed - <{self.json_data['options']['cursorSpeed']}>")))
        list_view.append(ListItem(Label(f"Scroll Speed - <{self.json_data['options']['scrollSpeed']}>")))

        # ListViewをリフレッシュ
        list_view.refresh()
        self.key_list.refresh()
if __name__ == "__main__":
    # Run command
    # python -m key2cursor.tui.app
    app = TuiApp()
    app.run()