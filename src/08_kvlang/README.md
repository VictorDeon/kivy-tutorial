## KV Language

É uma linguagem de marcação no estilo QML, XML e JSON para construção de interfaces gráficas.

Seu objetivo é separar o código de interface visual do código da lógica de negócio.

A linguagem kvlang existe somente para definir os widgets.

**Widget**: São todos os elementos (componentes) visuais e tudo que pode receber ou enviar eventos.

***
### Princípios da linguagem KV
***

1) O código KV pode ser aberto e executado automaticamente.

2) Sua nomeclatura é de acordo com a classe root da aplicação em minúsculo, aquela que herda a classe `App`

* MinhaApp(App) = minha.kv
* ProgramaApp(App) = programa.kv
* Principal(App) = principal.kv
* Exemplo02(App) = exemplo02.kv
* MeuProjetoMuitoDoido(App) = meuprojetomuitodoido.kv

3) O código KV pode ter somente um root (raíz)

4) Classes com o mesmo nome do arquivo kv serão automaticamente conectadas, com isso é possível acessar métodos da classe dentro do arquivo kv. O objetivo é ter a interface gráfica no arquivo KV e as regras de negócios no arquivo python.

***
### Keywords
***

O arquivo kv tem 3 keywords definidas que iremos utilizar quando precisar-mos utilizar:

1. `self`: O componente/widget que estamos editando
2. `root`: A classe que nos estamos implementado
3. `app`: A instância da aplicação

