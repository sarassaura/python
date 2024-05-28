'''
Implemente um algoritmo que declare uma matriz com 
a mesma quantidade de linhas e colunas (DEFINIDA pelo USUÁRIO). 
Preencha com 1 a DIAGONAL PRINCIPAL e com 0 as OUTRAS POSIÇÕES da matriz. 
Ao final, ESCREVA a matriz obtida na tela.

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas.
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Por exemplo,   

ENTRADAS 01:

5

SAÍDAS 01:

1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1

ENTRADAS 02:

2

SAÍDAS 02:

1 0
0 1

ENTRADAS 03:

10

SAÍDAS 03:

1 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0 1
'''

n = int(input())

m = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

for x in range(n):
    print(*m[x])