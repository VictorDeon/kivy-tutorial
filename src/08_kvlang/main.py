# flake8: noqa
import kivy
kivy.require("2.3.0")
from kivy.app import App
from screen01 import Screen01
from utils import Button


class MainApp(App):
    def exit(self):
        self.stop()


if __name__ == "__main__":
    app = MainApp()
    app.run()
