from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class MyInterface(MDBoxLayout):
    pass


class ThemesApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        return

ThemesApp().run()