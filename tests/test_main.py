from textual.app import App
from key2cursor.tui.widgets import mouse_center
from textual.binding import Binding
from textual.widgets import Footer, Header


class AppTest(App):
    TITLE = "Key2Cursor"
    BINDINGS = [
        Binding("q", "quit", "Quit the app"),
        Binding("question_mark", "help", "Show help screen", key_display="?"),
        Binding("delete", "delete", "Delete the thing"),
        Binding("j", "down", "Scroll down", show=False),
    ]
    CSS_PATH = r"mouse_center.tcss"

    def compose(self):
        yield Header()
        yield Footer()
        yield mouse_center.MouseWidget()

if __name__ == "__main__":
    # Run command
    # python -m tests.test_main
    app = AppTest()
    app.run()