'''
Faça um programa que leia um número inteiro n, 
crie e mostre uma matriz n x n triangular superior 
com valores iguais a 1. Uma matriz triangular superior possui 
apenas os elementos acima da diagonal principal 
diferentes de zero. Veja os exemplos de saída. 

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.


Exemplo de Entrada 1:
2

Saída 1:
0 1
0 0

Exemplo de Entrada 2:
3

Saída 2:
0 1 1
0 0 1
0 0 0

Exemplo de Entrada 3:
4

Saída 3:
0 1 1 1
0 0 1 1
0 0 0 1
0 0 0 0
'''

n = int(input())

m = [[0 for j in range(n)] for i in range(n)]

for x in range(n):
    for y in range(n):
        if x + n - y - 1 >= n:
            m[y][x] = 1

for z in range(n):
    print(*m[z])
