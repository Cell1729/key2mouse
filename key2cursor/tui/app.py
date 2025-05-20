from textual.app import App
from textual.binding import Binding
from textual.widgets import Footer, Header, Button, Label, ListItem, ListView
from textual.containers import Horizontal, Vertical, Container

# memo
# ListViewで現在のキーボードを表示する
# Buttonでマウスのボタンごとにキーバインドを表示する。
# 具体的にはマウスボタンを押下、したときにキーバインドを入力する画面を作成し入力できるようにする。

class AppTest(App):
    TITLE = "Key2Cursor"
    BINDINGS = [
        Binding("q", "quit", "Quit the app"),
        Binding("question_mark", "help", "Show help screen", key_display="?"),
        Binding("delete", "delete", "Delete the thing"),
        Binding("j", "down", "Scroll down", show=False),
    ]
    CSS_PATH = r"style.tcss"

    def compose(self):
        yield Header()
        yield Footer()
        yield Container(
                ListView(
                ListItem(Label("Left Click - <mouse mode + left>")),
                ListItem(Label("Right Click - <mouse mode + right>")),
                ListItem(Label("Scroll Up - <mouse mode + up>")),
                ListItem(Label("Scroll Down - <mouse mode + down>")),
                ListItem(Label("Side Button 1 - <mouse mode + side1>")),
                ListItem(Label("Side Button 2 - <mouse mode + side2>")),
            ),
            classes="bordered-list",
        )
        yield Container(
            Horizontal(
                Vertical(
                    Button("Side1", id="side_button1"),
                    Button("Side2", id="side_button2"),
                    classes="side-buttons",
                ),
                Container(
                    Horizontal(
                        Vertical(
                            Button("Left Click", id="left_click"),
                        ),
                        Vertical(
                            Button("Scroll Up", id="scroll_up"),
                            Button("Scroll Down", id="scroll_down"),
                        ),
                        Vertical(
                            Button("Right Click", id="right_click"),
                        ),
                        classes="main-mouse-buttons",
                    ),
                    classes="main-mouse-frame",
                ),
                Vertical(
                    Button("Mouse Mode", id="mouse_mode"),
                    classes="mouse-mode",
                ),
            ),
            classes="bordered-buttons",
        )

if __name__ == "__main__":
    # Run command
    app = AppTest()
    app.run()