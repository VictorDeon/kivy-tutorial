#coding: utf-8
from kivy.app import App
from kivy.uix.label import Label


def build():
    """
    Realiza o build do app hello world.
    """

    return Label(text="Hello World")


if __name__ == "__main__":
    hello_world = App()
    hello_world.build = build
    hello_world.run()