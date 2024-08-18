from kivy.uix.boxlayout import BoxLayout

KVLANG = """
<Screen02>:
    orientation: "vertical"
    Button:
        text: f"Clique {root.clicked_btn} vez"
        id: btn01
        # Aqui acessamos o método on_press_btn definida na classe Screen02
        on_press: root.on_press_btn()
"""


class Screen02(BoxLayout):
    clicked_btn = 1

    def on_press_btn(self):
        if self.clicked_btn > 1:
            self.ids.btn01.text = f"Fui clicado {self.clicked_btn} vezes"
        else:
            self.ids.btn01.text = f"Fui clicado {self.clicked_btn} vez"

        self.clicked_btn += 1
