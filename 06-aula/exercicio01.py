#! /usr/bin/env python3

import sys


def imprimir_linhas(arquivo):
    with open(arquivo, "r") as arq:
        for linha in arq.readlines():
            print(linha.strip())


if __name__ == '__main__':
    arquivo = sys.argv[1]
    imprimir_linhas(arquivo)
    
    
