import argparse
import subprocess
import signal
import sys
from key2cursor.tui.app import TuiApp
import time

controller_process = None

def start_keyboard_mouse_controller():
    """keyboard_mouse_controllerをバックグラウンドで起動する"""
    global controller_process
    if controller_process is None or controller_process.poll() is not None:
        controller_process = subprocess.Popen(
            [sys.executable, "-m", "key2cursor.keyboard_mouse_controller"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("keyboard_mouse_controllerを起動しました。")

def stop_keyboard_mouse_controller():
    """keyboard_mouse_controllerを停止する"""
    global controller_process
    if controller_process is not None and controller_process.poll() is None:
        controller_process.terminate()
        controller_process.wait()
        print("keyboard_mouse_controllerを停止しました。")

def main():
    parser = argparse.ArgumentParser(description="Key2Mouse CLI")
    parser.add_argument(
        "command",
        nargs="?",
        default="controller",
        help="コマンドを指定してください (デフォルト: controller)"
    )

    args = parser.parse_args()

    if args.command == "tui":
        # controllerを停止してTUIを起動
        stop_keyboard_mouse_controller()
        app = TuiApp()
        app.run()
        # TUI終了後にcontrollerを再起動
        start_keyboard_mouse_controller()
    elif args.command == "controller":
        # keyboard_mouse_controllerを起動
        start_keyboard_mouse_controller()
    else:
        print(f"不明なコマンド: {args.command}")
        parser.print_help()

if __name__ == "__main__":
     main()
