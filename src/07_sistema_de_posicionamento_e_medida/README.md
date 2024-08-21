## Posicionamento

O sistema de posicionamento do kivy segue o plano cartesiano `X`, `Y` sendo que o `X=0` e `Y=0` fica no canto inferior esquerdo da tela.

![Capturar](https://github.com/user-attachments/assets/2ebdb595-1ebb-47de-8af7-beb58df73d9d)

Só é exibido na tela os itens que tiver o posicionamento de `X` e `Y` maior que zero e menor que o limite de resolução da tela.

A resolução da tela é o valor máximo em X e Y que a tela pode chegar em pixel. Ex: resolução 1280x720 quer dizer que a tela pode chegar a 1280 pixels na horizontal (eixo X) e 720 pixels na vertical (eixo Y) do plano cartesiano, se passar disso fica fora da tela.

Os widgets terão seu ponto de origem tb no lado inferior esquerdo, ou seja, quem desloca em X e Y é o ponto de origem do widget que é o canto inferior esquerdo do widget.

- O canto inferior esquerdo do widget terá [X, Y]
- O canto superior esquerdo do widget terá [X, Y + Height]
- O canto inferior direito do widget terá  [X + Width, Y]

**Grid Layout**: Os componentes vão se ajustando em blocos e se dimensionando automaticamente a medida que forem crescendo.

Podemos usar como referência para o posicionamento no plano cartesiano dos widgets o centro, topo e o canto superior direito também.

#### Sufixo HINT

Propriedades com sufixo hint significam que os valores devem ser definidos em percentual.

Exemplo:
- `pos_hint: {'x': .1, 'y': .09}`: É a propriedade que espera um dicionário com os eixos X e Y associados a valores percentuais. 

Os valores percentuais devem estar no intervalo de 0.0 a 1.0

Exemplo:
- 1.0 = 100%
- 0.01 = 1%

#### X e Y

São as propriedades que definem as dimensões em pixels, são elas que determinam o posicionamento do widget no vídeo.

Exemplo:
- `x: 100` (100px da esquerda para a direita do video)
- `y: 350` (350px de baixo para cima do vídeo)

#### POS

É a propriedade que recebe uma tupla onde o primeiro valor é atribuído à propriedade `x` e o segundo a propriedade `y`

Exemplo:
- `pos: dp(80), dp(200)`

#### right

Essa propriedade permite realizar o posicionamento tendo o ponto de origem a margem direita do widget.

right = x + width

Exemplo:

```py
pos_hint: {'right': 1.}
```

```py
right: 300
y: 0
```

#### top

Essa propriedade permite realizar o posicionamento tendo o ponto de origem o topo do widget.

top = y + height

Exemplo:

```py
pos_hint: {'top': 1.}
```

```py
x: 200
top: 400
```

#### center

Essa propriedade permite realizar o posicionamento tendo o ponto de origem no centro do widget.

- center_x = x + (width/2)
- center_y = y + (height/2)

Exemplo:

```py
pos_hint: {'center': 1.}
```

```py
center_x: 200
certer_y: 100
```

```py
center: 200, 100
```

## Sistemas de Medida:

- **Pixel (px)**: Medida padrão

- **Pixel Independente de Densidade (dp)**: Faz com que o nosso botão seja exibido físicamente com o mesmo tamanho independente da resolução da tela. Garante o mesmo posicionamento e dimensão, indiferente da resolução da tela.

- **Escala Independente de Pixel (sp)**: É o sistema de medida do tamanho da fonte, funciona igual ao DP.

#### Valor percentual

Propriedades com sufixo hint significam que os valores devem ser definidos em percentual.

As propriedades `size_hint_x` e `size_hint_y` definem as dimensões percentuais para cada eixo do plano catertesiano.

Exemplo:
- `size_hint_x: .2`: É o tamanho width em porcentagem do elemento.
- `size_hint_y: .4`: É o tamanho height em porcentagem do elemento.
- `size_hint: .2, .4`: É o tamanho width e height em porcentagem do elemento.

Os valores percentuais devem estar no intervalo de 0.0 a 1.0

Exemplo:
- 1.0 = 100%
- 0.01 = 1%

#### Valor absoluto

A propriedade `width` especifica a largura absoluta e a `height` a altura absolute;

Temos a propriedade `size` que especifica a largura e altura absoluta como uma tupla.

Temos que definir o `size_hint` como `None` para poder definir o valor absoluto.

Exemplo:

```py
size_hint_x: None
width: 200
```

```py
size_hint_y: None
height: 300
```

```py
size_hint: None, None
size: 200, 300
```