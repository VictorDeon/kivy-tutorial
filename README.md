## Tutorial de Kivy
***

Baixe a extensão:

* EditorConfig for VS Code
* KvLang
* Python

***
### Kivy
***

#### Onde as configurações do kivy é criado em cada S.O

É um conjunto de propriedades que é lida pela aplicação quando a mesma é executada.

* **Windows**: C:\Users\\`<username>`\\.kivy\config.ini
* **OS X**: /Users/`<username>`/.kivy/config.ini
* **Linux**: /home/`<username>`/.kivy/config.ini
* **Android**: /data/data/org.kivy.launcher/files/.kivy/config.ini
* **iOS**: `<HOME_DIRECTORY>`/Documents/.kivy/config.ini

#### Modulo inspect

Dentro do arquivo `config.ini` podemos definir o seguinte código para fazer debug, só lembre-de remove-lo no deploy.

```
[module]
inspect =
```

Com isso dentro da aplicação ao dar `Ctrl + E` irá aparecer um widget para inserção dos elementos da tela muito útil para o desenvolvimento.

O ideal é modificar essas configurações dentro da sua aplicação caso for necessário.

```py
from kivy.config import Config
Config.set("class", "key", "value")
Config.set("modules", "inspect", "")
```

#### Modulo screen

Vamos simular as características de algum dispositivo ao executar o projeto.

```sh
# Lista os screens disponíveis
python main.py -m screen
# Simula o screen
python main.py -m screen:<device-id>
```

Ao executar, será exibido no console a lista de todos os screens que estão cadastrados.

#### Modulo console

Analisa a estrutura hierarquica de componentes de uma janela.

Dentro do arquivo `config.ini` devemos definir o seguinte código, só lembre-de remove-lo no deploy.

```
[module]
console =
```

Com isso dentro da aplicação ao dar `Ctrl + E` irá aparecer um widget, nesse widget tem um botão `Tree` que nos permite ver a estrutura hierarquica de componentes da aplicação. bastente útil para desenvolvimento para ver o fluxo de passagem de telas.