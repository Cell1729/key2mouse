from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Button, Label, ListItem, ListView, Static
from textual.containers import Horizontal, Vertical, Container

# memo
# ListViewで現在のキーボードを表示する
# Buttonでマウスのボタンごとにキーバインドを表示する。
# 具体的にはマウスボタンを押下、したときにキーバインドを入力する画面を作成し入力できるようにする。

class App(App):
    TITLE = "Key2Cursor"
    BINDINGS = [
        Binding("q", "quit", "Quit the app"),
        Binding("question_mark", "help", "Show help screen", key_display="?"),
        Binding("delete", "delete", "Delete the thing"),
        Binding("j", "down", "Scroll down", show=False),
    ]
    CSS_PATH = r"style.tcss"

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


if __name__ == "__main__":
    # Run command
    app = App()
    app.run()