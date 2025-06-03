from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Input, Label, Static
from textual.containers import Container
from textual import events
from textual.css.query import NoMatches
from key2cursor.config_manager import ConfigManager


class InputKeyOverlay(Screen):
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
        align: center middle;
    }
    .label-container {
        align: center middle;
    }
    """
    BINDINGS = [("escape", "app.pop_screen")]
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
                yield Container(Label(f'Input key "{self.key_name}".\nPress the key you want to set.\nescape : cancel', id="input_label"), classes="label-container")

    def on_key(self, event: events.Key) -> None:
        if event.key == "escape":
            # escキーの場合は通常の処理を行う
            self.app.pop_screen()
        else:
            # escキー以外のキーイベントを無効化
            event.prevent_default()
            event.stop()

            # 押下されたキーをJSONに保存
            pressed_key = event.key
            self.json_config.save_keybind(self.key_id, pressed_key)

            # コールバックがあれば実行
            if self.callback:
                self.callback()

            # オーバーレイを閉じる
            self.app.pop_screen()