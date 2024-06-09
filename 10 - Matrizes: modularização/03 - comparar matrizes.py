'''
Escreva a função comparar_matrizes que recebe duas matrizes 
(matriz1 e matriz2) e retorne True, caso a matriz2 tem 
todos os valores duplicados nas posições correspondentes da matriz1. 
Caso contrário, deve-se retornar False. Se as dimensões da matriz1 forem 
diferentes das dimensões da matriz2, a função deve retornar False.

Por exemplo, a função deve retornar True para as duas matrizes a seguir:

11 22
33 44

22 44
66 88


Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, entre outras.
'''

def comparar_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        return False
    if len(matriz1) == 0:
        return True
    
    lines = len(matriz1)
    columns = len(matriz1[0])

    for x in range(lines):
        for y in range(columns):
            if 2 * matriz1[x][y] != matriz2[x][y]:
                return False
    
    return True