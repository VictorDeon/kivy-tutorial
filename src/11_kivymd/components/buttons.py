from kivy.lang import Builder
from kivy.properties import DictProperty
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        MDIconButton:
            icon: "language-python"
        MDFloatingActionButton:
            icon: "android"
            md_bg_color: app.theme_cls.primary_color
        MDFlatButton:
            text: "MDFlatButton"
            theme_text_color: "Custom"
            text_color: "orange"
        MDRaisedButton:
            text: "MDRaisedButton"
            md_bg_color: "red"
        MDRectangleFlatButton:
            text: "MDRectangleFlatButton"
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "red"
        MDRectangleFlatIconButton:
            icon: "android"
            text: "MDRectangleFlatIconButton"
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "red"
            theme_icon_color: "Custom"
            icon_color: "orange"
        MDRectangleFlatIconButton:
            text: "MDRectangleFlatIconButtonWithoutBorder"
            icon: "language-python"
            line_color: 0, 0, 0, 0
        MDRoundFlatButton:
            text: "MDRoundFlatButton"
            text_color: "white"
        MDRoundFlatIconButton:
            text: "MDRoundFlatIconButton"
            icon: "android"
            text_color: "white"
        MDTextButton:
            text: "MDTextButton"
            custom_color: "white"
        MDFloatingActionButtonSpeedDial:
            id: speed_dial
            right_pad: True
            data: app.data
            root_button_anim: True
            hint_animation: True
            bg_hint_color: app.theme_cls.primary_dark
'''


class Example(MDApp):
    data = DictProperty()

    def callback(self, *args):
        print(args)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        self.data = {
            'Python': 'language-python',
            'JS': [
                'language-javascript',
                "on_press", lambda x: print("pressed JS"),
                "on_release", lambda x: print(
                    "stack_buttons",
                    self.root.ids.speed_dial.stack_buttons
                )
            ],
            'PHP': [
                'language-php',
                "on_press", lambda x: print("pressed PHP"),
                "on_release", self.callback
            ],
            'C++': [
                'language-cpp',
                "on_press", lambda x: print("pressed C++"),
                "on_release", lambda x: self.callback()
            ],
        }
        return Builder.load_string(KV)


Example().run()