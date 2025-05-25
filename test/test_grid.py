from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Container


class GridLayoutExample(App):
    CSS_PATH = "grid_layout2.tcss"

    def compose(self) -> ComposeResult:
        yield Static("", classes="box")
        yield Container(Button("up", classes="button"), classes="cell-center")
        yield Static("", classes="box")
        yield Container(Button("left", classes="button"), classes="cell-center")
        yield Static("Center", classes="box")
        yield Container(Button("right", classes="button"), classes="cell-center")
        yield Static("", classes="box")
        yield Container(Button("down", classes="button"), classes="cell-center")
        yield Static("", classes="box")


if __name__ == "__main__":
    app = GridLayoutExample()
    app.run()