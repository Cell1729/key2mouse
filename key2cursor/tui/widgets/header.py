from textual.app import App, ComposeResult
from textual.widgets import Header


class HeaderWidget(App):
    def compose(self) -> ComposeResult:
        yield Header()

    def on_mount(self) -> None:
        self.title = "Key2Cursor"


if __name__ == "__main__":
    app = HeaderWidget()
    app.run()