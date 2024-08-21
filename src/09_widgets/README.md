## Widgets

Todos os componentes widgets (Button, Label, ...) são filhos da classe `Widgets`. E essa que implementa a questão de posicionamento e dimensão dos widgets.


***
### Float Layout
***

Nesse layout os componentes serão posicionados pela definição de suas coordenadas geográficas dentro do plano cartesiano nos eixos X e Y e definir a largura e altura de cada widget dentro do layout.

![Capturar](https://github.com/user-attachments/assets/2ebdb595-1ebb-47de-8af7-beb58df73d9d)

Podemos ter mais infomações do atributos desse layout no tutorial de número 07_sistema_de_posicionamento_e_medidas.

***
### Box Layout
***

Organiza os componentes em uma determinada orientação, ou seja, organiza todos os componentes na vertical ou na horizontal. O posicionamento dos componentes é calculado e definido automaticamente pelo gerenciador de layout `BoxLayout`, porém as dimensões poderão ser definidos em valores absolutos ou percentuais

#### Orientação vertical:

![Capturar](https://github.com/user-attachments/assets/ffc47fdb-bdd6-4cb7-8997-a0f72d07d5d1)

#### Orientação horizontal

![Capturar](https://github.com/user-attachments/assets/1e4c245f-310c-4b0b-a62e-baba2ecc7b02)

***
### Stack Layout
***

Organiza os componentes de tal forma que os mesmos sejam empilhados um em cima do outro. Podemos empilhar de cima para baixo e de baixo para cima, da direita para esquerda e vise-versa.

![Capturar](https://github.com/user-attachments/assets/26dfea8c-0168-4df6-9008-36d71eb23d54)

A propriedade orientation pode assumir 8 valores:

* lr-tb (left-right e top-bottom)
* tb-rl (top-bottom e right-left)
* rl-tb (right-left e top-bottom)
* tb-lr (top-bottom e left-right)
* rl-bt (right-left e bottom-top)
* bt-lr (bottom-top e left-right)
* lr-bt (left-right e bottom-top)
* bt-rl (bottom-top e right-left)

Se a stack passar do tamanho da tela ela vai continuar sem dar error, porém a tela não vai mostrar o restante que ultrapassar.