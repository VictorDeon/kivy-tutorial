from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp

Builder.load_string('''
<ExampleBanner@Screen>
    MDBanner:
        id: banner
        type: "two-line-icon"
        icon: f"../themes/imgs/vksoftware-icon-512.png"
        text: ["One line string text example without actions.", "Oloko meu"]
        over_widget: screen
        vertical_pad: toolbar.height
        left_action: ["CANCEL", lambda x: self.hide()]
        right_action: ["CLOSE", lambda x: self.hide()]

    MDTopAppBar:
        id: toolbar
        title: "Example Banners"
        elevation: 4
        pos_hint: {'top': 1}

    MDBoxLayout:
        id: screen
        orientation: "vertical"
        size_hint_y: None
        height: Window.height - toolbar.height

        OneLineListItem:
            text: "Banner without actions"
            on_release: banner.show()

        Widget:
''')


class Test(MDApp):
    def build(self):
        return Factory.ExampleBanner()


Test().run()