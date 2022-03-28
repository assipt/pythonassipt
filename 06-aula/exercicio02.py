#! /usr/bin/env python3

import argparse


def imprimir_linhas(arquivo, linha_inicio=0, linha_fim=-1):
    with open(arquivo, "r") as arq:
        i = 0
        for linha in arq:
            if i >= linha_inicio and (linha_fim < 0 or i < linha_fim):
                print(linha.strip())
            i = i + 1
            if i == linha_fim:
                break
                

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Imprimir linhas")
    parser.add_argument('arquivo', help="Nome do arquivo", type=str, nargs=1)
    parser.add_argument("-i", "--inicio", help="Número da primeira linha para imprimir 0 caso não seja fornecido.", default=0, type=int)
    parser.add_argument("-f", "--fim", help="Número da última que deve ser impressa. -1 para imprimir até o final", default=-1, type=int)

    args = parser.parse_args()
    
    imprimir_linhas(args.arquivo[0], args.inicio, args.fim)
    
    
    
    
    
