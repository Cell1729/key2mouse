from pystray import Icon, MenuItem, Menu
from PIL import Image
import threading
from key2cursor.tui.app import TuiApp
from key2cursor.keyboard_mouse_controller import KeyboardMouseController

class MainApp:
    def __init__(self, image):
        self.keyboard_mouse_controller = KeyboardMouseController()
        self.status = False

        # アイコンの画像
        image = Image.open(image)
        # 右クリックで表示されるメニュー
        menu = Menu(
            MenuItem('Start Controller', self.start_controller),
            MenuItem('Open TUI', self.open_tui),
            MenuItem('Exit', self.stop_program),
        )

        self.icon = Icon(name='nameTray', title='titleTray', icon=image, menu=menu)

    def start_controller(self):
        if not self.status:
            self.status = True
            threading.Thread(target=self.keyboard_mouse_controller.keyboard_observer, daemon=True).start()

    def stop_controller(self):
        if self.status:
            self.status = False

    def open_tui(self):
        # Controllerを停止
        self.stop_controller()
        # TUIを起動
        app = TuiApp()
        app.run()
        # TUI終了後にControllerを再起動
        self.start_controller()

    def stop_program(self, icon):
        self.stop_controller()
        self.icon.stop()

    def run_program(self):
        self.icon.run()


if __name__ == '__main__':
    system_tray = MainApp(image=r"image/icon.png")
    system_tray.run_program()