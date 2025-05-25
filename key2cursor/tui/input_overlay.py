from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input, Label, Static
from textual.containers import Container
from textual import events
from textual.css.query import NoMatches
from key2cursor.config_manager import ConfigManager


class InputOverlay(Screen):
    CSS = """
    .overlay-container{
        align: center middle;
    }
    #overlay_box {
        width: 50%;
        height: 50%;
        border: solid green;
        align: center middle;
        background: $background 90%;
        layout: grid;
        grid-size: 3;
    }
    #input_label {
        width: 100%;
        height: auto;
        align: left bottom;
    }
    #ok_btn {
        border: solid $foreground;
        width: 20%;
        height: auto;
        align: center middle;
    }
    .btn-container {
        align: right top;
    }
    .label-container {
        align: left bottom;
    }
    .input-container {
        align: center middle;
        column-span: 3;
    }
    """
    OVERLAY_KEYMAP = {
        "enter" : "ok_btn",
    }
    BINDINGS = [("escape", "app.pop_screen", "キャンセル")]
    def __init__(self, key_name: str, key_id: str, int_only: bool = False, callback=None):
        super().__init__()
        self.key_name = key_name
        self.key_id = key_id
        self.int_only = int_only
        self.json_config = ConfigManager()
        self.callback = callback

    def compose(self) -> ComposeResult:
        with Container(classes="overlay-container"):
            with Container(id="overlay_box"):
                yield Container(Label(f'Input key "{self.key_name}"', id="input_label"), classes="label-container")
                yield Static("")
                yield Static("")
                yield Container(Input(placeholder="input here", id="keyboard_input"), classes="input-container")
                yield Static("")
                yield Static("")
                yield Container(Button("OK", id="ok_btn"), classes="btn-container")

    def on_button_pressed(self, event):
        """ボタンが押下されたときの処理"""
        value = self.query_one("#keyboard_input", Input).value
        if self.int_only:
            if not value.isdigit():
                # 数値以外は受け付けない
                self.query_one("#input_label", Label).update("Please enter integer numbers only")
                return
            value = int(value)
            self.json_config.save_value(self.key_id, value)
        else:
            self.json_config.save_keybind(self.key_id, value)

        if self.callback:
            self.callback()
        self.app.pop_screen()

    def on_key(self, event: events.Key) -> None:
        def press(button_id: str) -> None:
            """Press a button, should it exist."""
            try:
                self.query_one(f"#{button_id}", Button).press()
            except NoMatches:
                pass

        key = event.key
        button_id = self.OVERLAY_KEYMAP.get(key)
        if button_id is not None:
            press(self.OVERLAY_KEYMAP.get(key, key))
