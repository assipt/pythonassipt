


#%%
## Variáveis string

"Esta é uma cadeia de caracteres"
'Esta também é!'

#%% 
# Strings têm comprimento
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

base = "arquivo_"
ext = "txt"

ndig = 4
i = 1999

nome = base + f"{10**ndig + i}"[1:] + "." + ext
print(nome)


#%%
## Entrada de dados

s = input("Digite algo: ")

#%%
anos = int(input("Entre com tua idade: "))
meupi = float(input("Entre com o valor aproximado de pi: "))



