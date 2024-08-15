from kivy.app import App


class MeuProject(App):
    """
    O sistema de posicionamento do kivy segue o plano cartesiano X, Y
    sendo que o X=0 e Y=0 fica no canto inferior esquerdo da tela.
    
    Só é exibido na tela os itens que tiver o posicionamento de X e Y
    maior que zero e menor que o limite de resolução da tela.

    A resolução da tela é o valor máximo em X e Y que a tela pode chegar em pixel. Ex:
    resolução 1280x720 quer dizer que a tela pode chegar a 1280 pixels na horizontal (eixo X)
    e 720 pixels na vertical (eixo Y) do plano cartesiano, se passar disso fica fora da tela.
    
    Os widgets terão seu ponto de origem tb no lado inferior esquerdo, ou seja, quem
    desloca em X e Y é o ponto de origem do widget que é o canto inferior esquerdo do widget.
    - O canto inferior esquerdo do widget terá [X, Y]
    - O canto superior esquerdo do widget terá [X, Y + Height]
    - O canto inferior direito do widget terá  [X + Width, Y]

    Grid Layout: Os componentes vão se ajustando em blocos e se dimensionando
    automaticamente a medida que forem crescendo.

    Sistemas de Medida:
    - Pixel (px): Medida padrão
    - Pixel Independente de Densidade (dp): Faz com que o nosso botão seja exibido físicamente com o mesmo tamanho
    independente da resolução da tela. Garante o mesmo posicionamento e dimensão, indiferente da resolução da tela.
    - Escala Independente de Pixel (sp): É o sistema de medida do tamanho da fonte, funciona igual ao DP.
    """

    def build(self):
        """
        Realiza o build do app.
        """

        return None


if __name__ == "__main__":
    app = MeuProject()
    app.run()