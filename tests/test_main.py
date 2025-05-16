from textual.app import App
from textual.widgets import Header, Footer

class AppTest(App):
    def compose(self):
        yield Header()
        yield Footer()


if __name__ == "__main__":
    # Run command
    # python -m tests.test_main
    app = AppTest()
    app.run()