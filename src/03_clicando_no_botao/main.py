from kivy.app import App
from kivy.uix.button import Button


def click():
    """
    Executado ao clique do botão e exibir na saida padrão
    """

    print("O Botão foi clicado.")


def build():
    """
    Realiza o build do app.
    """

    btn = Button(text="Clique me")
    btn.on_press = click
    return btn


if __name__ == "__main__":
    app = App()
    app.build = build
    app.run()