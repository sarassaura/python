'''
Escreva um programa que leia um valor n e 
os elementos de uma matriz de inteiros com 
dimensões n x n (linha a linha). Depois, 
o programa deve calcular a 
soma dos elementos acima da diagonal principal. 

Por exemplo, para uma matriz com n=3, definida a seguir, 
a saída do programa deverá ser: "A soma eh: 12", 
pois acima da diagonal principal estão 
3 elementos com valores 5, 3 e 4. 
Portanto, a soma é 5 + 3 + 4 = 12.

1 5 3
8 9 4
7 5 3

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

n = int(input())

m = [[0 for i in range(n)] for j in range(n)]

for x in range(n):
    for y in range(n):
        m[x][y] = int(input())

sum = 0

for x in range(n):
    for y in range(n):
        if x + y >= n:
            sum += m[n - 1 - x][y]

print(f"A soma é: {sum}")