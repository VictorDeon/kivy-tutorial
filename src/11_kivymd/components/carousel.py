from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:
    MDCarousel:
        id: carousel
        direction: 'right'

        FitImage:
            source: "imgs/1.png"

        FitImage:
            source: "imgs/2.png"

        FitImage:
            source: "imgs/3.png"
'''

class CarouselApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    CarouselApp().run()
