import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.lang import Builder

from kivy.config import Config
Config.set("graphics", "fullscreen", "0")

KV = """
BoxLayout:
    Button:
        size_hint: .1, .1
        text: "A"
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    app = MainApp()
    app.run()
