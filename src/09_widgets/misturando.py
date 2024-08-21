import kivy
kivy.require("2.3.0")
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import logging


Window.clearcolor = (1, 1, 1, 1)  # RGBA

KV = """
#:import color kivy.utils.get_color_from_hex

# Inserindo background color usando canvas
<Box@FloatLayout>:
    canvas.before:
        Color:
            rgba: color("#151cdb")
        Rectangle:
            pos: self.pos
            size: self.size

GridLayout:
    cols: 2
    rows: 3
    padding: 20
    spacing: 10
    Button:
        text: "Button A"
        size_hint: .3, None
        background_color: 0, .2, .1, 1  # RGBA
        background_normal: ""
    Button:
        text: "Button B"
        size_hint: .3, None
        background_color: color("#43fd34")
    Box:
        BoxLayout:
            orientation: "vertical"
            Label:
                text: "Estudando a classe [size=25]Label[/size] 01"
                font_size: 15
                markup: True
            Label:
                text: "Estudando a classe [s]Label[/s] 02"
                font_name: "consola"
                markup: True
            Label:
                text: "Estudando a classe [i]Label[/i] [color=ff3333]03[/color]"
                bold: True
                markup: True
            Label:
                text: "Estudando a classe [b]Label[/b] [sup]04[/sup]"
                italic: True
                markup: True
            Label:
                text: "Estudando a classe [u]Label[/u] [sub]05[/sub]"
                color: .1, .2, .3, 1
                markup: True
            Label:
                text: "Estudando a classe Label 06"
                disabled: True
            Label:
                text: "Estudando a classe Label com muitas linhas " \
                    "muito doidas 07"
                text_size: 300, None
                halign: "center"
                valign: "middle"
    # Todas as propriedades de label pode ser usada em button
    Button:
        text: "Button [u]C[/u]"
        bold: True
        markup: True
        on_press: app.on_press_btn()
        on_release: app.on_release_btn()
"""


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)
    
    def on_press_btn(self):
        logging.info("APP: Fui clicado")

    def on_release_btn(self):
        logging.info("APP: Fim do clique")


if __name__ == "__main__":
    app = MainApp()
    app.run()
