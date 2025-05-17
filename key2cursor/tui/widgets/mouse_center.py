from textual.app import ComposeResult
from textual.widgets import Button
from textual.widget import Widget
from textual.containers import Horizontal, Vertical

class MouseWidget(Widget):
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Button("Side Button1", id="side_button1"),
                Button("Side Button2", id="side_button2"),
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