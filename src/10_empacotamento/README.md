## Empacotamento

O empacotamento ou Freeze é a ação de gerar executáveis nativos que serão acionados sem a necessidade de instalar o python. O kivy pode gerar executaveis para os 5 principais e mais usados sistemas operacionais:

* Windows
* Macos
* Linux
* Android
* IOS

Basicamente o empacotamento de aplicações e adição de todas os arquivos e informações necessárias para a sua correta execução dentro de um único arquivo, no caso um arquivo executavel.

***
### Alguns problemas do contexto de empacotamento atual
***

Cada sistema operacional possui usuários utilizando diversas versões e cada versão poderá estar sob a arquitetura de 32 ou 64 bits. Ou seja, precisamos gerar executaveis para 32 e 64 bits.

Outro problema é a versão 2x ou 3x do python e em cada uma delas temos de 32 e 64 bits.

Para cada sistema operacional também precisamos definir a versão mínima que o app serã instalado. Ex: Windows 10 ou macos 12 ou linux 22.04.

***
### Ferramentas para empacotamento
***

* **Android**: python-for-android
* **IOS**: kivy-ios
* **Android e IOS**: Buildozer
* **Windows, Mas e Linux**: PyInstaller

***
### Executavel
***

É um arquivo vinculado a um programa capaz de interpretar as suas informações. Ex: windows (.exe)
