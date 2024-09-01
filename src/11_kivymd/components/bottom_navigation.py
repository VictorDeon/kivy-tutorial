from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDBottomNavigation:
        # panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            icon: 'gmail'
            badge_icon: "numeric-10"
            on_tab_touch_down: print("on_tab_touch_down")
            on_tab_touch_move: print("on_tab_touch_move")
            on_tab_touch_up: print("on_tab_touch_up")
            on_tab_press: print("on_tab_press")
            on_tab_release: print("on_tab_release")

            MDLabel:
                text: 'Mail'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Twitter'
            icon: 'twitter'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'Twitter'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'LinkedIn'
            icon: 'linkedin'

            MDLabel:
                text: 'LinkedIn'
                halign: 'center'
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Test().run()