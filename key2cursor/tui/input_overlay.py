from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input, Label
from textual.containers import Container
from textual import events
from textual.css.query import NoMatches


class InputOverlay(Screen):
    CSS = """
    #overlay_box {
        width: 100%;
        height: 100%;
        border: solid green;
        align: center middle;
        background: $background 90%;
    }
    """
    NAME_MAP = {
        "enter" : "ok_btn",
    }
    BINDINGS = [("escape", "app.pop_screen", "キャンセル")]

    def compose(self) -> ComposeResult:
        # Containerで装飾や中央寄せ、枠線も作れる
        with Container(id="overlay_box"):
            yield Label("Input key", id="input_label")
            yield Input(placeholder="ここに入力", id="commit_input")
            yield Button("OK", id="ok_btn")

    def on_button_pressed(self, event):
        # 入力結果の取得と画面を閉じる
        value = self.query_one("#commit_input", Input).value
        self.app.pop_screen()

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
