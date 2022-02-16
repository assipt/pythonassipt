+++
title = "01 - Introdução e primeiros passos"
slug = "01-introducao-e-primeiros-passos"
date = "2022-01-31 20:41:11 UTC-03:00"
tags = "Python,instalação,spyder"
category = ""
link = ""
description = "Primeira aula introduzindo Python"
type = "text"
has_math = "yes"
+++

## Porque programar

Você está aqui então já deve ter alguma noção da importância e utilidade de programar. Se a tua ferramenta básica de trabalho é o Excel, o Python pode te ajudar. Não vai substituir o Excel necessariamente mas pode ajudar a fazer análise de dados mais aprofundadas. E tem os gráficos: os gráficos de excel são feios pra caramba!

Talvez você queira automatizar algo. Fazer um app para o telefone celular. Ou simplesmente comunicar com um arduino.

## Você já é um programador sem saber!

Sempre que você planeja algo você está programando. Quebre a tarefa em partes pequenas que são mais simples e facilmente realizadas. No computador isso é o que você faz com um programa de computador.

<!-- TEASER_END -->

## Linguagem de programação

Isso assusta né? O computador e o microprocessador usam códigos binários para controlar sua operação. Isso é um pouco chato para pessoas mas não impossível. Ainda tem gente programando em assembler!

Um meio termo é usar uma linguagem de programação. É uma linguagem adequada para uma pessoa ler e escrever e adequada para o computador executar.

A boa notícia é que a linguagem de programação tem muitos elementos em comum com a linguagem falada e escrita. Tem sintaxe, tem semântica, tem palavras, gramática, etc. Melhor inda é uma linguagem cujas regras são precisas: não existem exceções e casos especiais. Além disso, tem um vocabulario pequeno! Você e outras pessoas podem criar palavras novas mas o vocabulário é bem pequeno comparado com uma linguagem humana natural.

De certo modo, se você fala português, você é capaz de programar!

## Qual a melhor linguagem?

Resposta simples: a que você sabe! Mas se você não sabe, como escolher?

 * O que teus colegas usam?
 * O que está disponível?
 * Quão adequado é o ecossistema?
 * As pessoas estão usando isso na tua área
 * Vai conseguir emprego?
 * É software livre?
 * etc

## Porque Python

Python é uma linguagem simples e bem apropriada para ser uma primeira linguagem para iniciantes. Mas Python não é um brinquedo. Tem muita coisa séria sendo feita em Python principalmente em ciência de dados e machine learning.

Python surgiu como uma linguagem de script mas suas qualidades incentivaram que os usuários levassem ela muito mais longe do que se poderia imaginar no começo.

Aqui listamos alguns benefícios da linguagem Python

 * Linguagem simples e de fácil aprendizado
 * Linguagem que prioriza a simplicidade e fácil leitura do código
 * Multiplataforma. Desde microcontroladores (mais ou menos) até supercomputadores
 * Muita gente usando em muitas áreas distintas
 * Ecossistema enorme. Bibliotecas e aplicativos em quase qualquer área.
 * Bom para a web
 * Dá para programar no celular
 * Praticamente um padrão em ciência de dados e machine learning
 * Usado por muitos ambientes para automatizar tarefas


 
## O Ambiente Spyder

Sistema de desenvolvimento integrado que permite editar código Python, executar o código, debugar e até visualizar os resultados.

 * Editor de texto
 * O terminal/console
 * Explorador de variáveis
 * Ajuda
 * Visualização

## Um primeiro gostinho de python

### O teu primeiro programa

```python-repl
In [1]: print("Oi mundo!")
Oi mundo!
```

O programinha acima é uma expressão com os seguintes componentes:

 * `print` - chamada de função
 * `(` e `)` - parênteses
 * `"` Aspas
 * `Oi mundo!` - mensagem

### Python como calculadora:

```python-repl
In [1]: 2+3
Out[1]: 5

In [2]: 5-3
Out[2]: 2

In [3]: 10 - 4 + 2
Out[3]: 8

In [4]: 2 * 10 # Multiplicação
Out[4]: 20

In [5]: 20 / 4 # Divisão
Out[5]: 5.0

In [6]: 10/4
Out[6]: 2.5

In [7]: 10 // 4 # Divisão inteira
Out[7]: 2

In [8]: 2**3 # Potência
Out[8]: 8

```

**Importante**: Existe uma diferença entre divisão e divisão inteira. Também existe a função resto:

```python-repl
In [9]: 10 // 4
Out[9]: 2

In [10]: 10 % 4
Out[10]: 2

In [11]: (10 // 4) * 4 + (10 % 4)
Out[11]: 10

In [12]: 10 % 5
Out[12]: 0
```

Os operadores matemáticos seguem as mesmas regras de prioridade e execução que aprendemos na escola (mais ou menos). Ordem de prioridade:

 1. Exponenciação `**`
 2. Multiplicação `*` e divisão `/`, `//`, `%`
 3. Adição `+` e subtração `-`

A expressão 
\\[
1500 + \left(\frac{1500 \times 5\}{100}\right)
\\]

Pode ser escrita em Python como 

```python
1500 + 1500 * 5 / 100
```


Calcule a expressão usando lápis e papel.



## Canceito de variáveis e atribuição

Ficar digitando tudo sempre é chato e é muito fácil errar. Lembra das aulas de física na escola e o professor falava para fazer tudo literal? Em programação é a mesma coisa! Neste caso, dizemos que atribuímos um valor a uma variável.

**Programa 1**
```python
t = 10 # 1 - Tempo em s
g = 9.8 # 2 - Aceleração da gravidade m/s**2
z = 1/2 * g * t**2 # 3 - calcular a distância que cai
print(z) # Imprimir o resultado na tela
```


Salve o programa acima no editor de texto do Spyder (ou IDLE) e execute (tecla F5).


Também dá para digitar cada linha no terminal (IPython Console do spyder).


## Nomes de variáveis

Em Python, os nomes de variáveis devem começar com uma letra mas podem conter números ou sublinhados (_)

Exemplo de nomes válidos
```python
a1 = 1
velocidade = 2
Velocidade = 3
vel10 = 4
vel_media = 5
_xx_10_yy = 6  # Sublinhado é permitido
```

Exemplo de nomes não válidos 
```python
1a = 7
vel media = 8 # Erro espaço é especial!
```

## Variáveis numéricas

**Números inteiros**:
```python
1
0
-5
550
-47
1000
1_000
10_00
100_0
30000
30_000
1000000
1_000_000
-1_000_000
```

**Numéros de ponto flutuante**:
```python
1.0
0.0
3.14592
1_234.567
1e0
1e2
1e-1
1.1e-1
5.2345e-23
5.678e34
```


**Números binários, octais e hexadecimais**:

```python
a = 0b11 # Número binário
b = 0x0A # Número hexadecimal
c = 0o10 # Número octal
```


## Variáveis de tipo lógico

Álgebra booleana: `True` (verdadeiro) e `False` (falso).

```python
resultado = True
aprovado = False
```

### Operadores relacionais

```python
1 == 1
1 == 2
1 != 1
1 != 2
1 < 2
1 > 2
2 > 2
2 < 2
1 <= 1
1 >= 1
```

### Operadores lógicos

São os operadores `not` (negação), `and` (**E**), `or` (**OU**)

```python
not True
not False
True and True
True and False
False and True
False and False
True or True
True or False
False or True
False or False
```

### Epxressões lógicas

É possível combinar operadores lógicos com operadores relacionais.

Exemplo: Num brinquedo de parque de diversões, crianças só podem entrar se têm mais de 1.2 m de altura e 5 anos ou mais. O programa a seguir determina se a criança pode entrar no brinquedo

```python
idade = 4
altura = 1.3

permitido = idade >= 5 and altura >= 1.2
print(permitido)
```


## Variáveis string

Variáveis do tipo string armazenam cadeias de caracteres.

Para se representar uma string em Python, utiliza-se aspas duplas ou simples:

```python
"Esta é uma cadeia de caracteres"
'Esta também é!'
```

O tamanho de uma string é dada pelo número de caracteres. Isso pode ser obtido com a função `len`:

```python
len("A")
len("AB")
len("ABC")
len("A B")
len("A B C ")
```

É possível acessar os caracteres indexando o string:

```python-repl

In [32]: s = "ABCDEF"

In [33]: s[0]
Out[33]: 'A'

In [34]: s[1]
Out[34]: 'B'

In [35]: s[2]
Out[35]: 'C'

In [36]: s[3]
Out[36]: 'D'

In [37]: s[5]
Out[37]: 'F'

In [38]: s[6]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-38-c4bc18d4aa1b> in <module>
----> 1 s[6]

IndexError: string index out of range

```

### Operações com strings

#### Concatenação

```python-repl
In [39]: s = "ABC"

In [40]: s1 = s + "D"

In [41]: s1
Out[41]: 'ABCD'
```



### Composição

```python-repl
In [48]: idade = 10

In [49]: "João tem %d anos!" % idade
Out[49]: 'João tem 10 anos!'
```

 * `%d` para números inteiros
 * `%s` para strings
 * `%f` para números de ponto flutuante
 
```python-repl
In [55]: idade = 22

In [56]: "[%d]" % idade
Out[56]: '[22]'

In [57]: "[%03d]" % idade
Out[57]: '[022]'

In [58]: "[%3d]" % idade
Out[58]: '[ 22]'

In [59]: "[%-3d]" % idade
Out[59]: '[22 ]'
```

Para formatar pontos flutuantes (`float`)
```python-repl
In [64]: idade = 22.1

In [65]: "[%f]" % idade
Out[65]: '[22.100000]'

In [66]: "[%5f]" % idade
Out[66]: '[22.100000]'

In [67]: "[%5.2f]" % idade
Out[67]: '[22.10]'

In [68]: "[%5.3f]" % idade
Out[68]: '[22.100]'

In [69]: "[%5.1f]" % idade
Out[69]: '[ 22.1]'

In [70]: "[%10.2f]" % idade
Out[70]: '[     22.10]'
```

E agora podemos combinar tudo:

```python-repl

In [71]: nome = 'João'

In [72]: idade = 22

In [73]: grana = 51.34

In [74]: 

In [74]: "%s tem %d anos e R$%f no bolso" % (nome, idade, grana)
Out[74]: 'João tem 22 anos e R$51.340000 no bolso'

In [75]: "%s tem %d anos e R$%5.2f no bolso" % (nome, idade, grana)
Out[75]: 'João tem 22 anos e R$51.34 no bolso'
```


Existe um jeito mais "moderno" de se escrever isso:

```python-repl
In [85]: nome = 'João'

In [86]: idade = 22

In [87]: grana = 51.10

In [88]: "{} tem {} anos e R${} no bolso".format(nome, idade, grana)
Out[88]: 'João tem 22 anos e R$51.1 no bolso'

In [89]: "{} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)
Out[89]: 'João tem 22 anos e R$51.10 no bolso'

In [93]: "{:12s} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)
Out[93]: 'João         tem 22 anos e R$51.10 no bolso'

In [94]: "{:<12s} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)
Out[94]: 'João         tem 22 anos e R$51.10 no bolso'

In [95]: "{:>12s} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)
Out[95]: '        João tem 22 anos e R$51.10 no bolso'

```

Mais moderno ainda:

```python-repl
In [96]: nome = 'João'

In [97]: idade = 22

In [98]: grana = 51.10

In [99]: f"{nome} tem idade {idade} anos e R${grana} no bolso."
Out[99]: 'João tem idade 22 anos e R$51.1 no bolso.'

In [100]: f"{nome} tem idade {idade} anos e R${grana:5.2f} no bolso."
Out[100]: 'João tem idade 22 anos e R$51.10 no bolso.'
```


## Fatiamento de strings

```python-repl
In [101]: s = "ABCDEFGHI"

In [102]: s[0:1]
Out[102]: 'A'

In [103]: s[0:0]
Out[103]: ''

In [104]: s[0:3]
Out[104]: 'ABC'

In [105]: s[1:3]
Out[105]: 'BC'
```

Mas tem de vez em quando você quer ir até o fim ou até certo ponto



```python-repl
In [106]: s[3:]
Out[106]: 'DEFGHI'

In [107]: s[:3]
Out[107]: 'ABC'
```


Dá até para contar do final da string!


```python-repl
In [110]: s[-2]
Out[110]: 'H'

In [111]: s[0:-2]
Out[111]: 'ABCDEFG'

In [112]: s[-3:]
Out[112]: 'GHI'

In [113]: s[-3:-1]
Out[113]: 'GH'
```




## Entrada de dados

Função `input` lê uma string do terminal.

```python-repl
In [115]: s = input("Digite algo: ")
Digite algo: 1234
```

Muitas vezes queremos ler algo e converter para um número, inteiro ou float.



```python-repl
In [118]: anos = int(input("Entre com tua idade: "))
Entre com tua idade: 46

In [119]: anos
Out[119]: 46

In [120]: meupi = float(input("Entre com o valor aproximado de pi: "))
Entre com o valor aproximado de pi: 3.14

In [121]: meupi
Out[121]: 3.14
```



## Exercícios

### Exercício 1
 Converta as seguintes expressões matemáticas para Python e teste as no interpretador Python

 - \\(10 + 20 \times 30\\)
 - \\(4^2 \div 30 \\)
 - \\( (9^4 + 2) \times 6 - 1 \\)
 
### Exercício 2
 Digite a seguinte expressão no interpretador:

```python
10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
```

### Exercício 3
Faça um programa que escreve o teu nome na tela

### Exercício 4
Faça um programa que exibe o resultado de \\(2a\times 3b\\) onde a vale 3 e b vale 5.

### Exercício 5
Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.

### Exercício 6
Modifique o programa 1 de para se calcular o quanto uma pedra cai na lua após 5 s se a aceleração da gravidade na lua vale \\(g = 1,625\:m/s^2\\).


### Exercício 7
Qual o valor das expressões abaixo para a = 4, b=10, c=5.0, d=1 e f=5?

 - `a == c`
 - `a < b`
 - `d > b`
 - `c != f`
 - `a == b`
 - `c < d`
 - `b > a`
 - `c >= f`
 - `f >= c`
 - `c <= c`
 - `c <= f`

### Exercício 8
Qual o valo das expressões abaixo para `a = True`, `b = False` e `c = True`?

 - `a and b`
 - `b and a`
 - `not c`
 - `not d`
 - `not a`
 - `a and b`
 - `b and c`
 - `a or c`
 - `b or c`
 - `c or a`
 - `c or b`
 - `c or c`
 - `b or b`

### Exercício 9
Escreva um programa para determinar se uma pessoa deve ou não pagar imposto. Uma pessoa paga imposto se o salário é maior que R$ 1200.

### Exercício 10
Calcule o resultado da expressão para `A > B and C or D`


| A | B |   C   |   D   | Resultado |
|---|---|-------|-------|-----------|
| 1 | 2 | True  | False |           |
| 10| 3 | False | False |           |
| 5 | 1 | True  | False |           |

### Exercício 11
Escreva uma expressão para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias devem ser superiores a 7. Considere que o aluno cursa 3 materias e a nota de cada uma será armazenada nas variáveis `materia1`, `materia2`, `materia3`.


### Exercício 12
Tente concatenar uma string com um número inteiro

### Exercício 13
Faça um programa que peça dois números inteiros. Imprima na tela a soma desses números

### Exercício 14
Escreve um  programa que leia um valor em metros e o exiba na tela em milímetros.

### Exercício 15
Escreva um programa que leia uma quantidade de dias, horas e minutos e calcule o total de segundos

### Exercício 16
Escreve um programa que converta a temperatura digitada em °C em °F.


