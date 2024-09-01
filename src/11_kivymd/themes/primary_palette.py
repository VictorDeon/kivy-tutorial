from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDRectangleFlatButton:
        text: "Hello World"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

        return Builder.load_string(KV)


Example().run()