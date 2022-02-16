+++
title = "Pyodide"
slug = "pyodide"
date = "2022-02-08 14:42:39 UTC-03:00"
tags = ""
category = ""
link = ""
description = ""
type = "text"
+++

Alguém perguntou se existe alguma implementação Python na web. Quando se fala em tecnologias web, duas abordagens existem:

 - Server side
 - Client side

<!-- TEASER_END -->

Em um abordagem *server side* (lado do servidor), todo o processamento ocorre no servidor. É lógico que processar as coisas no cliente (navegador de internet em geral) é tem várias vantagens. Menos rede e menos processamento são usados. Mas aí em geral estamos limitados a Javascript, uma outra linguagem de programação importante que é padrão em praticamente em todos os navegadores. E aí tem um problema: teoricamente não faz diferença em que navegador um programa está rodando mas na prática cada navegador e cada versão têm suas peculiaridades.

Quando você roda as coisa no servidor, você tem controle total do que está acontecendo. Python é muito utilizado no servidor, assim como Java (outra linguagem de programação popular).

Existem alguns projetos que traduzem Python para javascript. Mas existe um projeto muito interessante que *usa o python original*!

Existe um padrão recente que se chama Web Assembly. É uma linguagem de baixo nível que, assim como Javascript, é suportado pelos principais navegadores. A implementação Python mais importante e usada é chamada de CPython e é o que estamos usando neste curso. Nesta implementação o interpretador é implementado em C (uma linguagem de programação de baixo nível extremamente importante). A sacada é que um programa em C pode ser compilado para Web Assembly.

O projeto [Pyodide](www.pyodide.org) fez exatamente isso: compilou o interpretador e várias outras bibliotecas Python (numpy e matplotlib) para web assembly. *Agora você pode rodar python no cliente*!!!

Se quiser brincar um pouco existe um terminal na web para você testar <https://pyodide.org/en/stable/console.html>.

O objetivo deste projeto é criar um ambiente para ciência de dados rodando no navegador.

Vale a pena ficar de olho...
