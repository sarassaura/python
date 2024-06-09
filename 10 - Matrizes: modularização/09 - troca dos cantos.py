'''
Escreva um programa que leia duas matrizes A e B, de inteiros, 
de dimensões 3x3. Depois, o seu programa deve trocar, 
entre as matrizes A e B, todos os elementos que 
estão nos cantos (vértices) dessas matrizes. 
Após a troca, o programa deve mostrar as matrizes A e B, 
com um espaço entre elas. 

Por exemplo, para a matriz de entrada A:
1 4 3
8 9 4
7 5 3

e matriz de entrada B:
2 5 3
7 8 4
9 5 2

seu programa deve imprimir:
2 4 3
8 9 4
9 5 2

1 5 3
7 8 4
7 5 3

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

a = [[0 for i in range(3)] for j in range(3)]
b = [[0 for i in range(3)] for j in range(3)]

for x in range(3):
    for y in range(3):
        a[x][y] = int(input())

for x in range(3):
    for y in range(3):
        b[x][y] = int(input())

vec = [0, 2]

for x in range(2):
    for y in range(2):
        temp = a[vec[x]][vec[y]]
        a[vec[x]][vec[y]] = b[vec[x]][vec[y]]
        b[vec[x]][vec[y]] = temp

for x in range(3):
    for y in range(3):
        print(a[x][y], sep=' ', end=' ')
    print()

print()

for x in range(3):
    for y in range(3):
        print(b[x][y], sep=' ', end=' ')
    print()