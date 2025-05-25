from textual import events
from textual.css.query import NoMatches
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Button, Label, ListItem, ListView, Static
from textual.containers import Vertical, Container
from input_overlay import InputOverlay

# memo
# ListViewで現在のキーボードを表示する
# Buttonでマウスのボタンごとにキーバインドを表示する。
# 具体的にはマウスボタンを押下、したときにキーバインドを入力する画面を作成し入力できるようにする。

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

    def compose(self) ->ComposeResult:
        yield Header()
        yield Footer()
        # Key Bindings List
        self.keylist =  Container(
            ListView(
                ListItem(Label("Move Up - <mouse mode + up>")),
                ListItem(Label("Move Down - <mouse mode + down>")),
                ListItem(Label("Move Left - <mouse mode + left>")),
                ListItem(Label("Move Right - <mouse mode + right>")),
                ListItem(Label("Left Click - <mouse mode + left>")),
                ListItem(Label("Right Click - <mouse mode + right>")),
                ListItem(Label("Scroll Up - <mouse mode + up>")),
                ListItem(Label("Scroll Down - <mouse mode + down>")),
                ListItem(Label("Cursor Speed - <50>")),
                ListItem(Label("Scroll Speed - <50>")),
            ),
            classes="bordered-list",
        )
        yield self.keylist
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
        self.keylist.border_title = "Key Bindings"
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
            pass
        elif event.button.id not in self.VALUE_KEY :
            self.push_screen(InputOverlay(self.BINDINGS_LIST[event.button.id]))
        else:
            # カーソルやスクロールの速度を入力する画面を表示
            # 整数のみを受付
            self.push_screen(InputOverlay(self.BINDINGS_LIST[event.button.id], int_only=True))

if __name__ == "__main__":
    # Run command
    app = TuiApp()
    app.run()