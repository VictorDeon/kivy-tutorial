from kivy.app import App
from kivy.uix.label import Label


def build():
    """
    Realiza o build do app.
    """

    label = Label(
        text="Curso de kivy",
        italic=True,
        font_size=50,  # px
    )
    label.bold = True
    label.color = "#FFF123"
    return label


if __name__ == "__main__":
    app = App()
    app.build = build
    app.run()