from kivy.uix.boxlayout import BoxLayout


class Screen02(BoxLayout):
    clicked_btn = 1

    def on_press_btn(self):
        if self.clicked_btn > 1:
            self.ids.btn01.text = f"Fui clicado {self.clicked_btn} vezes"
        else:
            self.ids.btn01.text = f"Fui clicado {self.clicked_btn} vez"

        self.clicked_btn += 1
