import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.lang import Builder

KV = """
GridLayout:
    cols: 2
    rows: 3
    # row_default_height: 50
    # row_force_default: True
    # col_default_width: 50
    # col_force_default: True
    Button:
        text: "A"
        size_hint: .3, None
    Button:
        text: "B"
        size_hint: .3, None
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
