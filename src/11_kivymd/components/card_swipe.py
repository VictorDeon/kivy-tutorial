from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe

KV = '''
<SwipeToDeleteItem>
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:
        padding: "8dp"
        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.remove_item(root)

    MDCardSwipeFrontBox:

        # Content of card.
        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True


MDScreen:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            elevation: 4
            title: "MDCardSwipe"

        MDScrollView:
            scroll_timeout : 100

            MDList:
                id: md_list
                padding: 0
'''


class SwipeToDeleteItem(MDCardSwipe):
    """
    Card with `swipe-to-delete` behavior.
    """

    text = StringProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def remove_item(self, instance):
        self.root.ids.md_list.remove_widget(instance)

    def on_start(self):
        '''Creates a list of cards.'''

        for i in range(20):
            self.root.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"One-line item {i}")
            )


Example().run()