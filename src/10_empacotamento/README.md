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

***
### Principais caracteristicas do empacotamento
***

1. O executavel servirá apenas para o SO em que foi gerado, ou seja, dentro do SO Windows só geramos executaveis para o Windows e não para o Linux ou Mac.

2. A quantidade de bits do python definirá os bits do SO, para um empacotamento de 64 bits temos que utilizar uma versão de 64 bits do python, e para 32 bits temos que usar a de 32 bits do python.

3. O executável suportará a versão atual e posteriores do SO. Ou seja, se empacotar no Windows 7 vai funcionar no Windows 10, porém o oposto não é garantido.

4. A versão do python é indiferente, ou seja, podemos utilizar a versão 2x ou 3x do python sem problema.

5. Devemos utilizar uma instalação do python limpa com um sistema operacional limpo para gerar o pacote.

***
### Arquivos .spec gerado pelo PyInstaller
***

```py
# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.building.build_main import Analysis # type: ignore
from PyInstaller.building.api import PYZ, EXE, COLLECT # type: ignore

# Faz a analise dos scripts python que estamos utilizando bem como suas dependencias
analysis = Analysis(
    scripts=['src\\main.py'],   # Uma lista de scripts especificados como ponto de entrada da aplicação.
    pathex=[],                  # Lista opcional de paths que serão pesquisados pelo python antes da execução do sys.path
    binaries=[],                # Podemos atribuir uma lista de binários adicionais, ou seja, arquivos .dll .so determinando que os mesmos devem ser adicionados ao empacotamento pois serão utilizados pela nossa aplicação.
    datas=[],                   # Podemos passar uma lista opcional de arquivos de dados, por exemplo, imagens, fontes e etc.
    hiddenimports=[],           # Lista adicional de modulos python que devem ser incluidos pois sabemos que o python não irá encontra-los.
    hookspath=[],               # Adiciona uma lista de hooks (implementações feitas por terceiros que tem por objetivo alterar o funcionamento de alguma aplicação)
    hooksconfig={},             # Adiciona configurações a serem usadas pelos hooks.
    runtime_hooks=[],           # Determina uma lista de scripts para serem utilizados como hooks em tempo de execução. Por exemplo, um script que é executado toda vez que a aplicação for iniciada.
    excludes=[],                # Determina uma lista de arquivos que não devem ser empacotados
    optimize=0,
)

# Cria um arquivo .zip que contém todos os módulos python puros
pyz = PYZ(analysis.pure)

# Gera o executável final do aplicativo (freeze)
exe = EXE(
    pyz,                                # Pyz com os módulos do python puro
    analysis.scripts,                   # Scripts de execução do projeto
    [],                                 # Outros scripts que devem ser inseridos dentro do executavel
    exclude_binaries=True,
    name='windows-pdf-split',           # Define o nome da aplicação
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,                      # Abre o console junto com a janela gráfica
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# No modo --ondir cria a pasta de saída com todos os arquivos necessários
collect = COLLECT(
    exe,                        # Insere o arquivo executável na pasta gerada
    analysis.binaries,          # Insere os binários na pasta gerada
    analysis.datas,             # Insere os arquivos definidos no datas na pasta gerada
    strip=False,
    upx=True,
    upx_exclude=[],
    name='src',                 # Nome da pasta gerada
)
```

***
### Arquivos .toc gerados na pasta build pelo PyInstaller
***

Arquivos TOC são listas de path e arquivos para uso do PyInstaller. Ou seja, dentro deles encontramos o path de todos os arquivos que serão empacotados e como eles foram empacotados.

