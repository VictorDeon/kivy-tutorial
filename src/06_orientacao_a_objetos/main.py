from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import logging


class MeuProject(App):
    """
    Iniciando o projeto
    """

    def __click(self, text: str) -> None:
        """
        Executado ao clique do botão e exibir na saida padrão
        """

        logging.info(f"App: Foi digitado {text}")

    def build(self):
        """
        Realiza o build do app.
        """

        layout = FloatLayout()
        # x=0, y=0: Bottom, Left

        self.title = "Kivy Tutorial"

        label = Label(text="Insira seu texto: ")
        label.size_hint = None, None
        label.height = 30
        label.width = 100
        label.y = 500
        label.x = 300
        layout.add_widget(label)

        text_input = TextInput()
        text_input.size_hint = None, None  # Resetar o tamanho do widget
        text_input.height = 300
        text_input.width = 400
        text_input.y = 180
        text_input.x = 290
        layout.add_widget(text_input)

        btn = Button(text="Enviar ao log")
        btn.size_hint = None, None
        btn.height = 50
        btn.width = 200
        btn.y = 100
        btn.x = 290
        btn.on_press = lambda: self.__click(text_input.text)
        layout.add_widget(btn)

        return layout


if __name__ == "__main__":
    app = MeuProject()
    Window.size = 770, 500  # L x H
    app.run()