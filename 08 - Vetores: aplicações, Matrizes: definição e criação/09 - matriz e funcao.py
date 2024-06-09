'''
Faça um programa que leia um números inteiros N e 
crie uma matriz m de números inteiros com dimensão N x N. 
Cada elemento na matriz é dado em função dos índices da linha (l) 
e da coluna (c) da matriz, da forma m[l][c] = l^3 + 2l^2 * c^2 − 3lc + c3. 
Depois, o programa deve mostrar todos os valores na 
diagonal secundária da matriz. Veja o exemplo. 

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Exemplo:

Para a entrada N = 4, a matriz m é:

0 1 8 27
1 1 11 37
8 11 36 89
27 37 89 189

A diagonal secundária é:
27 11 11 27

Entrada:
4

Saída:
27 11 11 27
'''

n = int(input())

m = [[0 for i in range(n)] for j in range(n)]

for x in range(n):
    for y in range(n):
        m[x][y] = (x**3) + (2 * x**2 * y**2) - (3 * x * y) + (y**3)

for z in range(n):
    print(m[z][n-1-z], sep=' ', end=' ')