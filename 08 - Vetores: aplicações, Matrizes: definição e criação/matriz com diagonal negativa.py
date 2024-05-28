'''
Faça um programa que leia um número inteiro n, 
crie e mostre uma matriz n x n preenchida com zeros, 
em que a diagonal principal seja composta por números negativos 
começando em -1 (na extremidade superior esquerda) 
até -n (na extremidade inferior direita). 

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.


Exemplo de Entrada 1:
2

Saída 1:
-1 0
0 -2

Exemplo de Entrada 2:
3

Saída 2:
-1 0 0
0 -2 0
0 0 -3
'''

n = int(input())

m = [[0 for j in range(n)] for i in range(n)]

for x in range(n):
    m[x][x] = -1 * (x + 1)

for y in range(n):
    print(*m[y])