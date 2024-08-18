from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from screen02 import Screen02, KVLANG


class Screen01(BoxLayout):
    def on_press_btn(self):
        Builder.load_string(KVLANG)
        Window.remove_widget(Window)
        Window.add_widget(Screen02())
