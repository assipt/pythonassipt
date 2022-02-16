#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:25:02 2022

@author: pjabardo
"""

#%%
# Como executar algo apenas se
# uma condição for verdadeira?

x = 10

if x > 5: # Repare nos dois pontos!
    print(f"{x} é maior que 5!") # Indentação!!!
    print("Outra linha")
# Fim do bloco indentado!
print("Saiu do if!")

#%%
# Exemplo maior
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a>b:
    print("O primeiro valor é maior!")

if b>a:
    print("O segundo valor é maior!")
    
#%%
idade = int(input("Digite a idade do seu carro: "))
if idade < 3:
    print("Seu carro é novo.")

    if idade > 1:
        print("Seu carro é novo mas usado.")
    

#%%
# As duas condições acima são complementares!
idade=int(input("Entre com a idade do carro: "))
val = (idade <= 3) == (not (idade > 3))
print(val)


#%%
# Usando o `else`
idade=int(input("Entre com a idade do carro: "))
if idade > 3:
    print("Seu carro é velho")
else:
    print("Seu carro é novo")

#%%
# Exatamente igual ao caso anterio
idade=int(input("Entre com a idade do carro: "))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

#%%
# Vamos tentar detectar erros:
idade=int(input("Entre com a idade do carro: "))

if idade < 0:
    print("Acho que há um erro. Idade negativa?")
else:
    if idade <= 3:
        print("Seu carro é novo")
    else:
        print("Seu carro é velho")


#%%
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

#%%
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

