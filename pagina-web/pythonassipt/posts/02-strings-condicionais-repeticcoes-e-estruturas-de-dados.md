+++
title = "02 Strings, condicionais e repeticções"
slug = "02-strings-condicionais-repeticcoes-e-estruturas-de-dados"
date = "2022-02-08 17:05:38 UTC-03:00"
tags = ""
category = ""
link = ""
description = ""
type = "text"
has_math=true
+++


# Variáveis de tipo string

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

<!-- TEASER_END -->

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



## Composição

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


## Gerando nomes de arquivo

Imagina que você queira gerar arquivos numerados que aparecem em ordem no explorer. A primeira tentativa  seria fazer a sequência

 * `arquivo_1.xyz`
 * `arquivo_2.xyz`
 * ...
 * `arquivo_N.xyz`

Mas isso não vai funcionar bem! Se N for 12, a coisa vai aparecer da seguinte maneira:

 * `arquivo_1.xyz`
 * `arquivo_10.xyz`
 * `arquivo_11.xyz`
 * `arquivo_12.xyz`
 * `arquivo_2.xyz`
 * ...
 * `arquivo_9.xyz`

Como resolver isso? Exemplo com `N=12`

 * `arquivo_001.xyz`
 * `arquivo_002.xyz`
 * ...
 * `arquivo_009.xyz`
 * `arquivo_010.xyz`
 * `arquivo_011.xyz`
 * `arquivo_012.xyz`


Como fazer isso? Vamos quebrar o nome do arquivo em partes:

 * Nome base: No exemplo anterior é `arquivo_`
 * O número
 * ponto
 * extensão

```python-repl
In [9]: base = "arquivo_"
   ...: ext = "txt"
   ...: 
   ...: ndig = 3
   ...: i = 12
   ...: 
   ...: nome = base + f"{10**ndig + i}"[1:] + "." + ext
   ...: print(nome)
arquivo_012.txt
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

### Exercício 1
Tente concatenar uma string com um número inteiro

### Exercício 2
Faça um programa que peça dois números inteiros. Imprima na tela a soma desses números

### Exercício 3
Escreve um  programa que leia um valor em metros e o exiba na tela em milímetros.

### Exercício 4
Escreva um programa que leia uma quantidade de dias, horas e minutos e calcule o total de segundos

### Exercício 5
Escreve um programa que converta a temperatura digitada em °C em °F.


# Condições

Vimos as expressões relacionais e condicionais. Temos os elementos básicos para fazer decisões. Agora veremos como usar estas expressões para se tomar decisões.
Tomar decisão aqui quer dizer executar condicionalmente partes do código.

## `if`

```
if <condição>:
   # Executar o bloco indentado se a condição for verdadeira
   # Blocos são separados por identação!!!
```


```python-repl
In [5]: x = 10
   ...: 
   ...: if x > 5: # Repare nos dois pontos!
   ...:     print(f"{x} é maior que 5!") # Indentação!!!
   ...: # Fim do bloco indentado!
   ...: print("Saiu do if!")
10 é maior que 5!
Saiu do if!
```

```python-repl
In [6]: x = 1
   ...: 
   ...: if x > 5: # Repare nos dois pontos!
   ...:     print(f"{x} é maior que 5!") # Indentação!!!
   ...: # Fim do bloco indentado!
   ...: print("Saiu do if!")
Saiu do if!
```

Esse exemplo não é muito útil né? Qual o problema? *Nós sabemos o valor de `x` antes de executar o `if`! A gente sabe o que deve ser executado. Isso é apenas um exemplo para mostrar a sintaxe e como funciona. Num caso real, não conhecemos o valor de `x`: o valor pode vir do usuário, um banco de dados, internet ou algum instrumento ligado ao computador. O exemplo a seguir introduz este aspecto em um exemplo maior:

```python-repl
In [7]: a = int(input("Primeiro valor: "))
   ...: b = int(input("Segundo valor: "))
   ...: 
   ...: if a>b:
   ...:     print("O primeiro valor é maior!")
   ...: 
   ...: if b>a:
   ...:     print("O segundo valor é maior!")
   ...: 
Primeiro valor: 1
Segundo valor: 2
O segundo valor é maior!
```

E se mudarmos os valores?


```python-repl
In [8]: a = int(input("Primeiro valor: "))
   ...: b = int(input("Segundo valor: "))
   ...: 
   ...: if a>b:
   ...:     print("O primeiro valor é maior!")
   ...: 
   ...: if b>a:
   ...:     print("O segundo valor é maior!")
   ...: 
Primeiro valor: 2
Segundo valor: 1
O primeiro valor é maior!
```

### Exercício 6
O que acontece se `a == b`? Teste!



Vamos usar um outro exemplo:

```python-repl
In [10]: idade = int(input("Digite a idade do seu carro: "))
    ...: if idade <= 3:
    ...:    print("Seu carro é novo.")
    ...: 
    ...: if idade > 3:
    ...:    print("Seu carro é velho.")
    ...: 
Digite a idade do seu carro: 4
Seu carro é velho.
```

Outro valor:

```python-repl
In [11]: idade = int(input("Digite a idade do seu carro: "))
    ...: if idade <= 3:
    ...:    print("Seu carro é novo.")
    ...: 
    ...: if idade > 3:
    ...:    print("Seu carro é velho.")
    ...: 
Digite a idade do seu carro: 2
Seu carro é novo.
```

### Exercício 7
Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa cobrando R$ 5 por km/h acima de 80 km/h.

### Exercicio 8
Escreva um programa que lê três números e imprima o valor do maior



## `else`

No exemplo da idade do carro, você tem duas condições complementares.

 - No primeiro `if`, trata do carro novo: `idade <= 3`
 - Segundo `if`: `idade > 3`

Repare que
```python-repl
In [10]: idade = 10

In [11]: (idade <= 3) == (not (idade > 3))
Out[11]: True

In [12]: idade = 1

In [13]: (idade <= 3) == (not (idade > 3))
Out[13]: True
```

A relação anterior é sempre verdadeira. Este tipo de situação é tão comum que existe algo para facilitar escrever o programa:

```python
if condição:
   # Se a condição for verdadeira
   # Execute este bloco.
else:
   # Caso contrário, execute este bloco.
   # Aqui a condição é falsa!
```

Exemplo
   


```python-repl
In [14]: idade=int(input("Entre com a idade do carro: "))
    ...: if idade > 3:
    ...:     print("Seu carro é velho")
    ...: else:
    ...:     print("Seu carro é novo")
    ...: 
Entre com a idade do carro: 10
Seu carro é velho

In [15]: idade=int(input("Entre com a idade do carro: "))
    ...: if idade > 3:
    ...:     print("Seu carro é velho")
    ...: else:
    ...:     print("Seu carro é novo")
    ...: 
Entre com a idade do carro: 1
Seu carro é novo
```

Como são complementares, então podemos escrever deste jeito:

```python-repl
In [17]: idade=int(input("Entre com a idade do carro: "))
    ...: if idade <= 3:
    ...:     print("Seu carro é novo")
    ...: else:
    ...:     print("Seu carro é velho")
    ...: 
Entre com a idade do carro: 10
Seu carro é velho

In [18]: idade=int(input("Entre com a idade do carro: "))
    ...: if idade <= 3:
    ...:     print("Seu carro é novo")
    ...: else:
    ...:     print("Seu carro é velho")
    ...: 
Entre com a idade do carro: 1
Seu carro é novo
```

### Exercício 9
Brinque com os programas acima entrando diferentes valores

### Exercício 10
Escreva um programa que pergunte a distância que um passageiro vai percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R 0,45 para viagens mais longas


## Estruturas aninhadas

É possível compor os ifs acima. Voltando ao exemplo da idade do carro, A entrada de carros permite que o usuário entre com números negativos. Idade negativa não faz sentido, nesse caso deve-se informar que houve um erro. O resto é igual.


```python-repl
In [19]: idade=int(input("Entre com a idade do carro: "))
    ...: 
    ...: if idade < 0:
    ...:     print("Acho que há um erro. Idade negativa?")
    ...: else:
    ...:     if idade <= 3:
    ...:         print("Seu carro é novo")
    ...:     else:
    ...:         print("Seu carro é velho")
    ...: 
Entre com a idade do carro: 1
Seu carro é novo

In [20]: 

In [20]: idade=int(input("Entre com a idade do carro: "))
    ...: 
    ...: if idade < 0:
    ...:     print("Acho que há um erro. Idade negativa?")
    ...: else:
    ...:     if idade <= 3:
    ...:         print("Seu carro é novo")
    ...:     else:
    ...:         print("Seu carro é velho")
    ...: 
Entre com a idade do carro: 10
Seu carro é velho

In [21]: idade=int(input("Entre com a idade do carro: "))
    ...: 
    ...: if idade < 0:
    ...:     print("Acho que há um erro. Idade negativa?")
    ...: else:
    ...:     if idade <= 3:
    ...:         print("Seu carro é novo")
    ...:     else:
    ...:         print("Seu carro é velho")
    ...: 
Entre com a idade do carro: -1
Acho que há um erro. Idade negativa?
```

É possível ter mais casos. Imagine que a existam produtos de diferentes categorias e cada um tenha um preço:

| Catogoria | Preço |
| --------- | ----- |
|    1      | 10,00 |
|    2      | 18,00 |
|    3      | 23,00 |
|    4      | 26,00 |
|    5      | 31,00 |

O programa a seguir verifica o preço de acordo com a tabela:
```python
categoria=int(input("Digite a categoria: "))

if categoria == 1:
    preço = 10
else:
    if categoria == 2:
        preço = 18
    else:
        if categoria == 3:
            preço = 23
        else:
            if categoria == 4:
                preço = 26
            else:
                if categoria == 5:
                    preço = 31
                else:
                    print("Categoria errada!")
                    preço = 0

print(f"O preço do produto é: R${preço:6.2f}.")
```

## `elif`

A quantidade de indentação no programa anterior começa a ficar inconveniente.
Não só é chato de escrever mas pode atrapalhar a leitura do código.

Python tem uma solução! `elif`:

```python
categoria=int(input("Digite a categoria: "))

if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31
else:
    print("Categoria errada!")
    preço = 0

print(f"O preço do produto é: R${preço:6.2f}.")
```

Bem melhor né?

### Exercício 11
Escreva um programa que leia dois números e que pergunte qual operação o usuário quer realizar e calcule esta operação. As operações válidas são:

 - soma (`+`)
 - subtração (`-`)
 - multiplicação (`*`)
 - divisão (`/`)

### Exercício 12
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh conmsumida e o tipo de instalação:

 - `R`: residências
 - `I`: indústrias
 - `C`: comércios

Calcule o preço da conta de luz de acordo com as regras a seguir:

|     Tipo     | Faixa (kWh)   | Preço   |
| :----------- | :-----------: | -----:  |
| Residencial  | Até 500       | R$ 0,40 |
|              | Acima de 500  | R$ 0,65 |
| Comercial    | Até 1000      | R$ 0,55 |
|              | Acima de 1000 | R$ 0,60 |
| Industrial   | Até 5000      | R$ 0,55 |
|              | Acima de 5000 | R$ 0,60 |

# Repetições

Com o que aprendemos até agora dá para fazer algumas coisas. Não muitas mas é um começo. Uma coisa em que o computador é bom é fazer tarefas repetitivas. Olha que interessante: as pessoas em geral não curtem muito as tarefas repetitivas...

Até agora, para repetir algo tínhamos que escrevê-las nós mesmo. Sabe aquela pessoa que deixa o microfone aberto com o cachorro latindo, caminhão de gás latindo e vizinha gritando? Não dá né. Então vamos fazê-la escrever 10 vezes *Não vou deixar o microfone aberto na reunião!*:

```python
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
print("Não vou deixar o microfone aberto na reunião!")
```

Mas infelizmente com a pandemia e trabalho remoto, a pessoa vai fazer isso no computador e ela sabe usar o recurso *copiar e colar*. Então não vai ser muito sacrifício...

Que tal mandar ela fazer isso 1000 vezes? Aí pode ser um pouco melhor. Mas a gente não sabe que essa pessoa está aprendendo Python. Então ela escreve o seguinte programinha:

```python
msg = "Não vou deixar o microfone aberto na reunião!"
N = 1000
i = 1
while i <= N:
    print(msg)
    i = i + 1
```

Temos que reconhecer o esforço...


`while` é o comando básico de repetição e funciona da seguinte maneira:

```
while condição:
      # Enquanto a condição acima for verdadeira
      # Execute o bloco indentado aqui
```

Vamos voltar à solução do nosso intrépido usuário de Python:

 - Temos a variável `N` que é o número de repetições
 - Temos a variável `i` que será um contador
 _ Temos `while` com a condição `i <= N`. O bloco será repetido enquanto essa condição for verdadeira!
 - No bloco:
   * Imprimimos a mensagem `msg`
   * Fazemos uma coisa estranha: `i = i + 1`!!!

O sinal de igualdade: i = i + 1 ???

**Lembre-se `=` é um operador de atribuição e não de comparação**. O que estamos fazendo é atribuir um novo valor para i: o valor antigo somado a 1.

      
## Infinitas repetições

Esse tipo de comando para se gerar repetições é conhecido como laço ou *loop*. É muito comum cometer um erro e o laço não acabar. Nesse caso, o computador vai explodir (no Star Trek, série original). Para sair disso pression Ctrl-C.

```python
# Loop infinito
i = 0
while True:
    print(i)
    i = i + 1
```



### Exercício 13
Faça um programa para exibir os números de 1 a 100

### Exercício 14
Modifique o programa para exibir os números de 50 a 100

### Exercício 15
Escreva um programa que faz a contagem regressiva para o lançamento de um foguete: 10,9,...,1,Fogo


## Contadores

As variáveis `i` nos programas anteriores são *contadores* e são usados para se saber quando o loop deve acabar.

```python
fim = int(input("Digite o último número a imprimir: "))
x = 1
while x<= fim:
    print(x)
    x = x + 1
```

É possível combinar `while` e `if`. Vamos agora imprimir só os números pares:


```python
fim = int(input("Digite o último número a imprimir: "))
x = 0
while x<=fim:
    if x % 2 == 0:
        print(x)
    x = x + 1
```

Mas os contadores não precisam ir de um em um! Aqui está um jeito melhor:

### Exercício 16
Modifique os programas anteriores para imprimir os números ímpares.

### Exercício 17
Reescreva o programa para escrever os 10 primeiros múltiplos de 3

### Exercício 18
Escreve um programa que recebe um número e escreve a tabuada desse número. Exemplo do resultado para o número 2:

`2 x 1 = 2`

`2 x 2 = 4`

...

`2 x 10 = 20`


## Acumuladores

Muitas vezes além de contar, precisamos acumular valores. Exemplo: multiplicação de dois números naturais: 3 x 4 = 3 + 3 + 3 + 3

```python
x1 = int(input("Entreo com um inteiro: "))
x2 = int(input("Entreo com um inteiro: "))

resultado = 0
i = 1
while i <= x2:
    resultado = resultado + x1
    i = i + 1
    
print(f"{x1} x {x2} = {resultado}")
```


Também dá para fazer a divisão inteira e resto:

11 / 2: 11 - 2 - 2 - 2 - 2 - 2 = 1

Temos 5 subtrações (resultado da divisão inteira) e resto 1


```python
# Divisão
x1 = int(input("Entreo com um inteiro: "))
x2 = int(input("Entreo com um inteiro: "))

divisão = 0
total = x1
while total >= x2:
    total = total - x2
    divisão = divisão + 1

print(f"{x1} / {x2} = {divisão} com resto {total}")
```

### Exercício 19
Escreva um programa que calcula a divisão inteira entre dois números usando `+` apenas

## Operadores de atribuição especiais

Nos programas anteriores, usamos expressões do tipo

```python
i = i + 1
x = x - 1
```

Isso é tão comum que existem operadores especialisados:
```python
i = 10
i = i + 1
i = 10
i += 1 # Mesma operação

i = 10
i = i + 10
i = 10
i += 10 # Mesma operação

i = 10
i = i - 1
i = 10
i -= 1

i = 10
i = i - 5
i = 10
i -= 5

i = 10
i = i * 5
i = 10
i *= 5
```

Também existem os operadores `/=`, `**=`, `//=`, `%=`. A idéia é a mesma, se tivermos um operador binário `∘`, em geral existe o operador de atribuição `∘=` que quer dizer que `x = x ∘ y` é a mesma coisa que `x ∘= y`. *Não sei se são todos os operadores*.




### Exercício 20
Reescreva o programa de divisão acima com esses operadores de atribuição especial.


## Interrompendo a repetição

Use `break` para sair de um laço e `continue` para ir para a próxima iteração do laço.

Exemplo: um programa para somar uma sequência de números dados pelo usuário:


### Exercício 20
Escreva um programa que lê números do teclado. O programa deve ler os números até que o usuário digite 0 que indica que não se deseja entrar com mais números. Imprima a soma dos números, a quantidade de números digitada pelo usuário e a média aritmética dos números.


## Repetições aninhadas

Como tudo em Python, dá para combinar laços, um laço dentro do outro;

Exemplo: tabela de tabuada.

```python
tabuada = 1
while tabuada <= 10:
    num = 1
    print(f"Tabuada do {tabuada}")
    while num <= 10:
        print(f"{tabuada} x {num} = {tabuada*num}")
        num += 1
    print("")
    tabuada += 1
```

### Exercício 21
Escreva um programa que determina se um número é primo ou não. Um número é primo se ele é divisível por 1 e por ele mesmo apenas. Dica: use o operador resto (`%`) para saber se um número é divisível por outro.

### Exercício 22
Escreva um programa que recebe um número inteiro `n` e determina os primeiros `n` números primos


# Estruturas de dados: listas

Até este momento, trabalhamos com dados simples, números e strings. Os strings têm uma característica um pouco diferente: ele é composto por caracteres. Muitas vezes é interessante trabalhar com coleções de dados. Existem diversas maneiras de organizar estas coleções de dados. A mais simples é a lista.

Em python, uma lista é uma sequência de objetos:
```python
x = [1,2,3,4]
y = [1, 1.0, "um"]
```

A lista também pode conter listas!
```python
z = [1,2,3,4, ["a", "b"], [1,2,3,4], [1,[2,3,[4,5]]]]
```

Para se saber o comprimento de uma lista, use a função `len`:

```python-repl
In [23]: x = [1,2,3,4]
    ...: y = [1, 1.0, "um"]
    ...: z = [1,2,3,4, ["a", "b"], [1,2,3,4], [1,[2,3,[4,5]]]]

In [24]: print(len(x))
    ...: print(len(y))
    ...: print(len(z))
    ...: 
4
3
7
```

Para se acessar o n-ésimo elemento, use colchetes. Lembrando que em python, se conta a partir do zero!

```python-repl
In [26]: print(x[0])
    ...: print(x[1])
    ...: print(x[2])
    ...: print(x[3])
    ...: print(x[4])
    ...: 
1
2
3
4
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-26-8f8e192057fe> in <module>
      3 print(x[2])
      4 print(x[3])
----> 5 print(x[4])

IndexError: list index out of range
```


Atenção com estruturas de dados mais complexas, por exemplo listas que contém listas:

```python-repl
In [27]: print(z[0])
1

In [28]: print(z[3])
4

In [29]: print(z[4])
['a', 'b']

In [30]: print(z[4][0])
a

In [31]: print(z[6])
[1, [2, 3, [4, 5]]]

In [32]: print(z[6][0])
1

In [33]: print(z[6][1])
[2, 3, [4, 5]]

In [34]: print(z[6][1][2])
[4, 5]

In [35]: print(z[6][1][2][1])
5
```


Nota média:

```python
notas = [6, 6.5, 8.5, 7, 7.5]
soma = 0
N = len(notas)
i = 0
while i < N:
    soma += notas[i]
    i += 1
media = soma / N

print(f"A nota média é: {media:4.2f}")
```

### Exercício 23
Brinque com o programa acima, aumentando o número de notas e mudando o valor das notas.
