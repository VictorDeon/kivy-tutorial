"""
É uma linguagem de marcação no estilo QML, XML e JSON para construção de interfaces gráficas.
Seu objetivo é separar o código de interface visual do código da lógica de negócio.
A linguagem kvlang existe somente para definir os widgets.
Widget: São todos os elementos (componentes) visuais e tudo que pode receber ou enviar eventos.
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.metrics import dp


class MainApp(App):
    """
    O nome da classe tem que ser o mesmo
    nome do arquivo .kv com o sufixo App
    """

    def build(self):
        layout = FloatLayout()

        btn1 = Button()
        btn1.size_hint = None, None
        btn1.size = 350, 50
        btn1.x = 100
        btn1.y = 350
        btn1.text = "px"
        layout.add_widget(btn1)

        btn2 = Button()
        btn2.size_hint = None, None
        btn2.size = dp(350), dp(50)
        btn2.pos = dp(80), dp(200)
        btn2.text = "dp"
        layout.add_widget(btn2)

        btn3 = Button()
        btn3.size_hint = 0.5, 0.09
        btn3.pos_hint = {"x": 0.1, "y": 0.1}
        btn3.text = "%"
        layout.add_widget(btn3)

        return layout


if __name__ == "__main__":
    app = MainApp()
    app.run()
