from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    """
    Realiza o build do app.
    """

    return TextInput(text="Texto padrão")


if __name__ == "__main__":
    app = App()
    app.build = build
    app.run()