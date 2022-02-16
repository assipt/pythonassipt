
#%%
# Primeiro programa

print("Oi mundo!")


#%%
### Python como calculadora:

2+3
5-3
10 - 4 + 2

2 * 10 # Multiplicação

20 / 4 # Divisão

10/4

10 // 4 # Divisão inteira

2**3 # Potência

10 // 4

10 % 4

(10 // 4) * 4 + (10 % 4)

10 % 5


#%%
## Canceito de variáveis e atribuição

# Quanto que um corpo cai?
t = 10 # 1 - Tempo em s
g = 9.8 # 2 - Aceleração da gravidade m/s**2
z = 1/2 * g * t**2 # 3 - calcular a distância que cai
print(z) # Imprimir o resultado na tela


#%%

# Exemplo de nomes válidos
a1 = 1
velocidade = 2
Velocidade = 3
vel10 = 4
vel_media = 5
_xx_10_yy = 6  # Sublinhado é permitido

#%%

#Exemplo de nomes não válidos 
#1a = 7
#vel media = 8 # Erro espaço é especial!






#%%
## Variáveis numéricas

#**Números inteiros**:


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

#%%
#**Numéros de ponto flutuante**:
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

#%%
#Números binários, octais e hexadecimais

a = 0b11 # Número binário
b = 0x0A # Número hexadecimal
c = 0o10 # Número octal


#%%
# Variáveis de tipo lógico

resultado = True
aprovado = False

#%%
### Operadores relacionais

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

#%%
### Operadores lógicos

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



#%%
### Epxressões lógicas

idade = 4
altura = 1.3

permitido = idade >= 5 and altura > 1.2
print(permitido)

#%%
## Variáveis string

"Esta é uma cadeia de caracteres"
'Esta também é!'


len("A")
len("AB")
len("ABC")
len("A B")
len("A B C ")

#%%
s = "ABCDEF"
s[0]
s[1]
s[2]
s[3]
s[5]
s[6]

#%%
### Operações com strings

#### Concatenação

s = "ABC"
s1 = s + "D"
s1


#%%
### Composição

idade = 10
"João tem %d anos!" % idade

#%%
idade = 22
"[%d]" % idade
"[%03d]" % idade
"[%3d]" % idade
"[%-3d]" % idade

#%%
idade = 22.1
"[%f]" % idade
"[%5f]" % idade
"[%5.2f]" % idade
"[%5.3f]" % idade
"[%5.1f]" % idade
"[%10.2f]" % idade

#%%
nome = 'João'
idade = 22
grana = 1.34

"%s tem %d anos e R$%f no bolso" % (nome, idade, grana)
"%s tem %d anos e R$%4.2f no bolso" % (nome, idade, grana)

#%%
nome = 'João'
idade = 22
grana = 51.10

#%%
"{} tem {} anos e R${} no bolso".format(nome, idade, grana)
"{} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)
"{:12s} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)
"{:<12s} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)
"{:>12s} tem {} anos e R${:5.2f} no bolso".format(nome, idade, grana)

#%%
nome = 'João'
idade = 22
grana = 51.10

f"{nome} tem idade {idade} anos e R${grana} no bolso."
f"{nome} tem idade {idade} anos e R${grana:5.2f} no bolso."


#%%
## Fatiamento de strings

s = "ABCDEFGHI"
s[0:1]
s[0:0]
s[0:3]
s[1:3]

#%%
s[3:]
s[:3]

# Dá até para contar do final da string!

#%%
s[-2]
s[0:-2]
s[-3:]

s[-3:-1]




#%%
## Entrada de dados

s = input("Digite algo: ")

#%%
anos = int(input("Entre com tua idade: "))
meupi = float(input("Entre com o valor aproximado de pi: "))

