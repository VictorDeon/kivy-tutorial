from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from screen02 import Screen02


class Screen01(BoxLayout):
    def on_press_btn(self):
        Window.remove_widget(Window)
        Window.add_widget(Screen02())
