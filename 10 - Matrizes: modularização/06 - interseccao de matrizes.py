'''
Escreva um programa que leia duas matrizes A e B, de inteiros, 
de dimensões 3x3. Depois, o seu programa deve criar e 
mostrar uma outra matriz C que seja 
a intersecção das matrizes A e B. 
A matriz intersecção deve trazer valor zero se 
os elementos nas mesmas posições das matrizes A e B forem 
diferentes e, caso contrário, deve 
trazer o próprio elemento presente em A e B. 

Por exemplo, para a matriz de entrada A:
1 5 3
8 9 4
7 5 3

e matriz de entrada B:
2 5 3
7 8 4
9 5 2

a matriz C, a ser mostrada pelo programa será:
0 5 3
0 0 4
0 5 0

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

a = [[0 for i in range(3)] for j in range(3)]
b = [[0 for i in range(3)] for j in range(3)]
c = [[0 for i in range(3)] for j in range(3)]

for x in range(3):
    for y in range(3):
        a[x][y] = int(input())

for x in range(3):
    for y in range(3):
        b[x][y] = int(input())

for x in range(3):
    for y in range(3):
        if a[x][y] == b[x][y]:
            c[x][y] = a[x][y]
        else:
            c[x][y] = 0

for x in range(3):
    print(*c[x])