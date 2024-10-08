from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

# Your layouts.
Builder.load_string('''
#:import os os
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:import images_path kivymd.images_path


<ItemBackdropFrontLayer@TwoLineAvatarListItem>
    icon: "android"

    IconLeftWidget:
        icon: root.icon


<MyBackdropFrontLayer@ItemBackdropFrontLayer>
    backdrop: None
    text: "Lower the front layer"
    secondary_text: " by 50 %"
    icon: "transfer-down"
    on_press: root.backdrop.open(-Window.height / 2)
    pos_hint: {"top": 1}
    _no_ripple_effect: True


<MyBackdropBackLayer@Image>
    size_hint: .8, .8
    source: os.path.join(images_path, "logo", "kivymd-icon-512.png")
    pos_hint: {"center_x": .5, "center_y": .6}
''')

# Usage example of MDBackdrop.
Builder.load_string('''
<ExampleBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['menu', lambda x: self.open()]]
        title: "Example Backdrop"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Menu:"

        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: backlayer

        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
''')


class ExampleBackdrop(MDScreen):
    pass


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return ExampleBackdrop()


Example().run()