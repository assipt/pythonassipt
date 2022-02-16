+++
title = "Miniconda"
slug = "miniconda"
date = "2022-02-16 20:03:41 UTC-03:00"
tags = ""
category = ""
link = ""
description = ""
type = "text"
+++

Já falei que existem várias maneiras de se instalar o python. Em linux é bem fácil. No windows, principalmente quando você não tem acesso como administrador da máquina tem que ter algum cuidado.

Eu sugeri usar o WinPython <https://winpython.github.io>. É baixar, descompactar e usar. Mas as versões com mais coisas são bem grandes.

Uma outra alternativa é usar a distribuição de Python Anaconda <https://www.anaconda.com/products/individual>. Esta é a **melhor** alternativa! Mas também é gigantesco.

Outro dia eu mostro como instalar a partir dos binários oficiais do Python <https://www.python.org/downloads/windows/>.

Mas hoje quero mostrar uma alternativa bem legal sugerida por alguém na primeira aula: miniconda.
<!-- TEASER_END -->

## Miniconda

O Miniconda (<https://docs.conda.io/en/latest/miniconda.html>) é baseado no anaconda mas é minimalista. Enquanto que o anaconda instala um monte de coisas, o miniconda instala o Python e ferramentas mínimas, entre elas o *conda*.

*Conda* é um gerenciador de pacotes python. O que eu quero dizer com isso? É basicamente uma ferramenta que permite instalar e dar upgrade em pacotes/bibliotecas/etc python.

## Instalação

Neste link <https://docs.conda.io/en/latest/miniconda.html#windows-installers> você encontra instaladores do miniconda. Tente instalar com a versão mais recente de python (hoje é 3.9) mas **importante**>: *No windows 7, você só pode instalar até versão 3.8*!

Após instalar, procure algo como prompt do miniconda. Isso abrirá uma janela preta que trará saudades (ou pesadelos) para a velha guarda que apanhou do DOS.

Aí para instalar pacotes, basta executa o comando

```
conda install <nome-do-pacote>
```

Em particular, eu vou começar a usar os notebooks do Jupyter. Então execute o comando

```
conda install jupyter
```

Se quiser instalar o spyder:
```
conda install spyder
```

Acho que vocês já pegaram a idéia. Quando você quiser usar o Jupyter, você abre o prompt do miniconda e executa o seguinte comando:

```
jupyter notebook
```

Deve abrir o navegador e aí você já pode usar. Se o navegador não abrir, vai aparecer um endereço no prompt. Basta copiar e colar no seu navegador favorito.

Depois eu faço um vídeo disso.

Até a próxima aula.



