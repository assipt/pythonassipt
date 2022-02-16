#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:31:21 2022

@author: pjabardo
"""

#%%
msg = "Não vou deixar o microfone aberto na reunião!"
N = 1000
i = 1
while i <= N: 
    print(msg) 
    i = i + 1


#%%

i = 1
print(i)

i = i + 1
print(i)


i = i + 1
print(i)

#%%
# Loop infinito
i = 0
while True:
    print(i)
    i = i + 1

#%%
fim = int(input("Digite o último número a imprimir: "))
x = 1
while x<= fim:
    print(x)
    x = x + 1

#%%
fim = int(input("Digite o último número a imprimir: "))
x = 0
while x<=fim:
    if x % 2 == 0:
        print(x)
    x = x + 1

#%%
fim = int(input("Digite o último número a imprimir: "))
x = 0
while x<=fim:
    print(x)
    x = x + 2

#%%
x1 = int(input("Entreo com um inteiro: "))
x2 = int(input("Entreo com um inteiro: "))

resultado = 0
i = 1
while i <= x2:
    resultado = resultado + x1
    i = i + 1
    
print(f"{x1} x {x2} = {resultado}")

#%%

# Divisão
x1 = int(input("Entreo com um inteiro: "))
x2 = int(input("Entreo com um inteiro: "))

divisão = 0
total = x1
while total >= x2:
    total = total - x2
    divisão = divisão + 1

print(f"{x1} / {x2} = {divisão} com resto {total}")

#%%
# Divisão com soma
x1 = int(input("Entre com um inteiro: "))
x2 = int(input("Entre com um inteiro: "))

divisão = 0
total = x2
while total <= x1:
    total = total + x2
    divisão = divisão + 1

resto = total -x1
if resto == x2:
    resto = 0

print(f"{x1} / {x2} = {divisão} com resto {resto}")

#%%
# Break

soma = 0

while True:
    v = int(input("Digite um número para somar o zero para sair: "))
    if v == 0:
        break
    soma += v

print(f"A soma vale {soma}")

#%%
# Tabela de tabuada

tabuada = 1
while tabuada <= 10:
    num = 1
    print(f"Tabuada do {tabuada}")
    while num <= 10:
        print(f"{tabuada} x {num} = {tabuada*num}")
        num += 1
    print("")
    tabuada += 1

