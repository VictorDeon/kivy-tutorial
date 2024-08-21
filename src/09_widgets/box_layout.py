import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.lang import Builder

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 10
    Button:
        size_hint: 1., 1.
        text: "A"
    Button:
        size_hint: 1., 1.
        text: "B"
    Button:
        size_hint: 1., 1.
        text: "C"
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    app = MainApp()
    app.run()
