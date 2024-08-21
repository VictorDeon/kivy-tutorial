import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder

KV = """
StackLayout:
    orientation: "bt-lr"
    Button:
        size_hint: .33, .1
        text: "X1"
    Button:
        size_hint: .33, .1
        text: "X2"
    Button:
        size_hint: .33, .1
        text: "X3"
"""


class MainApp(App):
    def build(self):
        layout = Builder.load_string(KV)
        for i in range(20):
            layout.add_widget(Button(text=f"X{i+4}", size_hint=(.33, .1)))

        return layout


if __name__ == "__main__":
    app = MainApp()
    app.run()
