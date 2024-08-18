from kivy.uix.button import Button


def tabuada(self, x: int) -> None:
    self.text = f"{x} x {self.result} = {x * self.result}"
    self.result += 1



Button.result = 0
Button.tabuada = tabuada