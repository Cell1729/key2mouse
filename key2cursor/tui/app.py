from textual.app import App
from textual.binding import Binding
from textual.widgets import Footer, Header, Button, Label, ListItem, ListView
from textual.containers import Horizontal, Vertical


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
        yield ListView(
            ListItem(Label("Left Click")),
            ListItem(Label("Right Click")),
            ListItem(Label("Scroll Up")),
            ListItem(Label("Scroll Down")),
            ListItem(Label("Side Button 1")),
            ListItem(Label("Side Button 2")),
        )
        yield Horizontal(
            Vertical(
                Button("Side1", id="side_button1"),
                Button("Side2", id="side_button2"),
            ),
            Vertical(
                Button("Left Click", id="left_click"),
            ),
            Vertical(
                Button("Scroll Down", id="scroll_down"),
                Button("Scroll Up", id="scroll_up"),
            ),
            Vertical(
                Button("Right Click", id="right_click"),
            )
        )

if __name__ == "__main__":
    # Run command
    app = AppTest()
    app.run()