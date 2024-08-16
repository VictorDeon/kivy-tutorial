"""
É uma linguagem de marcação no estilo QML, XML e JSON para construção de interfaces gráficas.
Seu objetivo é separar o código de interface visual do código da lógica de negócio.
A linguagem kvlang existe somente para definir os widgets.
Widget: São todos os elementos (componentes) visuais e tudo que pode receber ou enviar eventos.
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class RootWidget(FloatLayout):
    pass


class MainApp(App):
    """
    O nome da classe tem que ser o mesmo
    nome do arquivo .kv com o sufixo App
    """

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    app = MainApp()
    app.run()
