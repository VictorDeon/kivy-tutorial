import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.lang import Builder

KV = """
FloatLayout:
    Button:
        size_hint: .1, .1
        pos_hint: {"x": 0, "top": 1.}
        text: "A"
    
    Button:
        size_hint: .2, .2
        pos_hint: {"center_x": .5, "center_y": .5}
        text: "B"

    Button:
        size_hint: .1, .1
        pos_hint: {"right": 1., "y": 0}
        text: "C"

    Button:
        size_hint: None, None
        pos_hint: {"center_y": .7}
        x: 150
        width: 200
        height: 100
        text: "Absoluto"
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    app = MainApp()
    app.run()
