#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:19:48 2022

@author: pjabardo
"""

#%% 
# listas

x = [1,2,3,4]
y = [1, 1.0, "um"]
z = [1,2,3,4, ["a", "b"], [1,2,3,4], [1,[2,3,[4,5]]]]
    
#%% 
print(len(x))
print(len(y))
print(len(z))

#%%
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

#%%
print(z[0])
print(z[3])
print(z[4])
print(z[4][0])
print(z[6])
print(z[6][0])
print(z[6][1])
print(z[6][1][2])
print(z[6][1][2][1])

#%% 
# Programa para calcular notas

notas = [6, 6.5, 8.5, 7, 7.5]
soma = 0
N = len(notas)
i = 0
while i < N:
    soma += notas[i]
    i += 1
media = soma / N

print(f"A nota média é: {media:4.2f}")

