+++
title = "Virtualenv e Pip"
slug = "virtualenv-e-pip"
date = "2022-04-07 16:08:02 UTC-03:00"
tags = "Python,pip,virtualenv,bibliotecas,pacotes,ambientes virtuais"
category = ""
link = ""
description = ""
type = "text"
+++

Apesar do python ter uma [bela biblioteca padrão](https://docs.python.org/pt-br/3/library/index.html), ainda falta muita coisa, principalmente quando se fala de aplicações científicas ou de ciências de dados. O que torna o Python tão popular nessas áreas não são apenas as características positivas da linguagem. Tão relevante quanto, são as bibliotecas externas associadas a essas áreas. [As bibliotecas básicas foram abordadas brevemente na aula 08 do curso:](/posts/aula-08-numpy-scipy-matplotlib-e-pandas)

 * Numpy <https://numpy.org/>
 * SciPy <https://scipy.org/>
 * Matplotlib <https://matplotlib.org/>
 * Pandas <https://pandas.pydata.org/>

<!-- TEASER_END -->

Por mais interessantes e abrangentes que essas bibliotecas sejam, elas ainda fornecem a funcionalidade básica para a área científica e de ciência de dados. Mas isso não se restringe apenas a esses setores importantes: Python é muito maior que a linguagem em si e sua biblioteca padrão. Lembrem-se do tamanho imenso de distribuições de Python como [Anaconda](https://www.anaconda.com/products/distribution) ou [WinPython](http://winpython.github.io/).

É difícil de imaginar alguma área onde não existam aplicativos e bibliotecas Python. Mas esta variedade e diversidade precisa ser gerenciada de alguma maneira. Foi-se o tempo em que cada projeto tinha uma página web e disponibilizava para download os arquivos do projeto. Essa abordagem se tornou insustentável quando começaram a surgir pacotes que dependiam de outros pacotes e assim por diante.

Hoje a comunidade Python tem ferramentas para gerenciar isso: PyPI.

## PyPI: Python Package Index <https://pypi.org/>

O [PyPI](https://pypi.org/) é um repositório que centraliza software relacionado com a linguagem Python. o PyPI ajuda você a encontrar e instalar software desenvolvido e compartilhado pela comunidade Python.

No momento em que escrevo isso, existem 368.139 projetos cadastrados. Mas o PyPI não é apenas um portal web para software Python. Está associado a ferramentas que

 * Ajudam a instalar o pacote
 * Ajudam a instalar as dependências dos pacotes
 * Ajudam a compilar e gerenciar dependências binárias (em geral códigos escritos C/C++/Fortran)
 * Ajudam a gerenciar o software e suas versões

## Instalando software com `pip`

A ferramente básica para instalação de pacotes python é o `pip`. Originalmente uma ferramente independente, hoje é parte da instalação básica do Python.

Para instalar o `numpy`, basta abrir um terminal e executar o seguinte comando:

```shell
pjabardo@makhno:~/temp$ python -m pip install numpy
Collecting numpy
  Using cached numpy-1.22.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
Installing collected packages: numpy
Successfully installed numpy-1.22.3
```

Muitas vezes existe um programa chamada `pip` e não precisamos digitar o `python -m pip`. Assim, para instalar um pacote (`scipy` agora) podemos fazer:

```shell
pjabardo@makhno:~/temp$ pip install scipy
Collecting scipy
  Using cached scipy-1.8.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (42.1 MB)
Requirement already satisfied: numpy<1.25.0,>=1.17.3 in ./pacotes/lib/python3.9/site-packages (from scipy) (1.22.3)
Installing collected packages: scipy
Successfully installed scipy-1.8.0
```

Tanto o `numpy` quanto o `scipy` usam bibliotecas em C/C++/Fortran mas o `pip` e toda a infraestrutura por trás no PyPI tomam conta disso. A não ser que você esteja trabalhando em uma plataforma pouco usual, você não terá problema com essas dependências binárias.

Uma outra coisa legal do `pip` é que ele baixa também todas as dependências de um projeto. Vamos usar como exemplo a biblioteca `matplotlib`:

```shell
pjabardo@makhno:~/temp$ pip install matplotlib
Collecting matplotlib
  Using cached matplotlib-3.5.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl (11.2 MB)
Collecting pyparsing>=2.2.1
  Using cached pyparsing-3.0.7-py3-none-any.whl (98 kB)
Collecting cycler>=0.10
  Using cached cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting pillow>=6.2.0
  Using cached Pillow-9.1.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.3 MB)
Collecting kiwisolver>=1.0.1
  Using cached kiwisolver-1.4.2-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
Collecting packaging>=20.0
  Using cached packaging-21.3-py3-none-any.whl (40 kB)
Collecting python-dateutil>=2.7
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Requirement already satisfied: numpy>=1.17 in ./pacotes/lib/python3.9/site-packages (from matplotlib) (1.22.3)
Collecting fonttools>=4.22.0
  Using cached fonttools-4.31.2-py3-none-any.whl (899 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, python-dateutil, pillow, packaging, kiwisolver, fonttools, cycler, matplotlib
Successfully installed cycler-0.11.0 fonttools-4.31.2 kiwisolver-1.4.2 matplotlib-3.5.1 packaging-21.3 pillow-9.1.0 pyparsing-3.0.7 python-dateutil-2.8.2 six-1.16.0
```

A biblioteca `matplotlib` usa a funcionalidade de outras bibliotecas como

 * `pyparsing`
 * `cycler`
 * `pillow`
 * E ainda alguns outros pacotes

Pode se ver acima que o `pip` baixou e instalou no lugar correto estas dependências.

Neste momento é possível imaginar um potencial problema na instalação de pacotes. Cada pacote é, em geral, desenvolvido de maneira independente. Novas funcionalidades podem ser acrescentadas, funcionalidade pode ser retirada e, muito comum, modificada. O problema nesse caso é que se você está usando um pacote que usa uma determinada versão de um outro pacote, se este outro pacote for modificado de maneira incompatível com a versão original, nada mais vai funcionar.

Para este tipo de situação, muito mais comum do que você pode imaginar, a comunidade Python criou uma outra ferramenta: `virtualenv`, hoje uma funcionalidade básica incorporada ao python.

Esta ferramente cria um ambiente onde o usuário pode instalar pacotes sem interferir diretamente na instalação básica do python. O usuário pode criar esse ambiente virtual na sua própria conta (recomendado) sem ter acesso de administrador da máquina. O usuário pode criar quantos ambiente virtuais quiser, geralmente um para cada projeto que ele estiver trabalhando.

Vamos criar um ambiente virtual para aplicações científicas. Para mostrar o que acontece vou criar um ambiente virtual chamado `ciencia` dentro de uma pasta vazia chamada `pasta`:

```shell
pjabardo@makhno:~/pasta$ ls
pjabardo@makhno:~/pasta$ python -m venv ciencia
pjabardo@makhno:~/pasta$ ls
ciencia
pjabardo@makhno:~/pasta$ ls ciencia/
bin  include  lib  lib64  pyvenv.cfg  share
pjabardo@makhno:~/pasta$ ls ciencia/bin/
activate      activate.fish  easy_install      pip   pip3.9  python3
activate.csh  Activate.ps1   easy_install-3.9  pip3  python  python3.9
```

O comando `python -m venv ciencia`, cria uma pasta `ciencia` dentro da pasta `pasta` como se pode ver acima. Dentro desta pasta, são criadas sub-pastas onde o mais importante é a pasta `ciencia/bin`. Nela você vê programas conhecidos: `pip` e `python`!

A pasta `lib` é onde são instaladas bibliotecas básicas e mais para frente as bibliotecas externas.

```shell
pjabardo@makhno:~/pasta$ ls ciencia/lib
python3.9
pjabardo@makhno:~/pasta$ ls ciencia/lib/python3.9/
site-packages
pjabardo@makhno:~/pasta$ ls ciencia/lib/python3.9/site-packages/
easy_install.py       pkg_resources-0.0.0.dist-info
pip                   __pycache__
pip-20.3.4.dist-info  setuptools
pkg_resources         setuptools-44.1.1.dist-info
```

### Usando o ambiente virtual no Linux

Está tudo criado mas o ambiente não está ativado. Para isso é necessário usar os scripts `ciencia/bin/activate` (ou algo parecido). Qual o script você vai usar depende do ambiente que você está trabalhando. Nesse caso estou usando Linux com o shell bash (terminal). Então para ativar este ambiente executo o seguinte comando:

```shell
pjabardo@makhno:~/pasta$ source ciencia/bin/activate
(ciencia) pjabardo@makhno:~/pasta$ which python
/home/pjabardo/pasta/ciencia/bin/python
(ciencia) pjabardo@makhno:~/pasta$ which pip
/home/pjabardo/pasta/ciencia/bin/pip
```

Repare no `(ciencia)` antes do `pjabardo@makhno`. Isso mostra qual o nome do ambiente está sendo utlizado. No Linux, o comando `which` mostra qual o caminho (endereço) exato de um comando e pode-se ver claramente que o ambiente está ativo. Da mesma maneira, o comando `pip` se refere ao ambiente virtual.

Agora, quando executarmos o comando `pip` os pacotes serão instalados dentro deste ambiente virtual:

```shell
(ciencia) pjabardo@makhno:~/pasta$ pip install numpy
Collecting numpy
  Using cached numpy-1.22.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
Installing collected packages: numpy
Successfully installed numpy-1.22.3
(ciencia) pjabardo@makhno:~/pasta$ ls ciencia/lib/python3.9/site-packages/
easy_install.py         pkg_resources
numpy                   pkg_resources-0.0.0.dist-info
numpy-1.22.3.dist-info  __pycache__
numpy.libs              setuptools
pip                     setuptools-44.1.1.dist-info
pip-20.3.4.dist-info
```

Olha que legal: o numpy foi instalado dentro deste ambiente separado. Neste ambiente virtual, pode-se instalar as versões mais recentes de pacotes ou versões de pacotes específicas (ver a documentação do `pip`).

### Ambientes virtuais no Windows

As coisas aqui são quase iguais. A única diferença é que para se ativar o ambiente virtual é necessário executar um arquivo .bat: `ciencia\bin\activate.bat`. De resto é tudo igual.

### Desativando ambientes virtuais

No final do trabalho, você pode querer desativar estes ambientes virtuais. Fechando o terminal funciona bem. Mas você pode executar o script `deactivate`:

```shell
(ciencia) pjabardo@makhno:~/pasta$ deactivate 
pjabardo@makhno:~/pasta$ 
```

## Sugestão de como trabalhar com Python

Quando se está começando a trabalhar com Python e se descobre a quantidade enorme de pacotes disponíveis para quase qualquer atividade, existe uma tentação de sair instalando de tudo com `pip`. Evite fazer isso pois pode haver incompatibilidades entre os diferentes pacotes. Se a incompatibilidade for grande, o `pip` nem vai deixar você instalar alguns pacotes. Este é o melhor cenário com tudo funcionando do jeito que deveria funcionar. No entanto é comum que existam incompatibilidades pequenas: é provável que ninguém nunca instalou os mesmos pacotes na mesma sequência que você!

Se você está usando Linux, o sistema operacional tem um gerenciador/instalador de software que provavelmente inclui a maioria dos pacotes Python relevantes. E a compatibilidade entre os pacotes foi bastante testada pelos desenvolvedores do sistema operacional. Instale por aí.

Outra possibilidade, tanto no Windows ou no Linux (ou MacOS), é usar a distribuição de Python Anaconda mencionado várias vezes ao longo do curso. Essa distribuição testa exaustivamente a compatibilidade entre pacotes e possui um gerenciador próprio: `conda`. Use e abuse disso.

Muitas vezes, você precisa usar o `pip`, seja porque o pacote não está disponível no Anaconda/sistema operacional ou você precisa da versão mais recente do pacote.  A minha recomendação é usar um ambiente virtual.

Como regra geral, **use `pip` sempre dentro de um ambiente virtual!**


