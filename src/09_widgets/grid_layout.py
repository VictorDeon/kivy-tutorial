import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)  # RGBA

KV = """
#:import color kivy.utils.get_color_from_hex

GridLayout:
    cols: 2
    rows: 3
    padding: 20
    spacing: 10
    Button:
        text: "A"
        size_hint: .3, None
        background_color: 0, .2, .1, 1  # RGBA
        background_normal: ""
    Button:
        text: "B"
        size_hint: .3, None
        background_color: color("#43fd34")
    Button:
        text: "C"
    Button:
        text: "D"
    Button:
        text: "E"
    Button:
        text: "G"
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    app = MainApp()
    app.run()
