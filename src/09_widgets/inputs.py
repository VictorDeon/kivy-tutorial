import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.lang import Builder
import logging

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 10

    TextInput:
        id: name_input
        hint_text: "Digite seu nome aqui"
        readonly: False
        font_name: "consola"
        font_size: 25
        foreground_color: .2, .5, .1, 1
        tab_width: 4
        write_tab: True
        padding: 30

    Button:
        text: "Enviar"
        on_press: app.send({ \
            "name": name_input.text, \
        })
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)
    
    def send(self, data: dict):
        logging.info(f"Dados enviados: {data}")


if __name__ == "__main__":
    app = MainApp()
    app.run()
