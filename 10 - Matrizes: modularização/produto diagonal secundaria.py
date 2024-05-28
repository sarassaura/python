'''
Escreva um programa que leia um valor n e 
os elementos de uma matriz de inteiros com 
dimensões n x n (linha a linha). Depois, 
o programa deve calcular o produto dos elementos 
na diagonal secundária da matriz. 

Por exemplo, para n=3 e a matriz a seguir, 
a saída do programa deverá ser: 
"O produto é: 189", pois 
na diagonal secundária estão 3 elementos 
com valores 3, 9 e 7. 
Portanto, o produto é 3 * 9 * 7 = 189.

1 5 3
8 9 4
7 5 3


IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

n = int(input())
m = [[0 for i in range(n)] for j in range(n)]
p = 1

for x in range(n):
    for y in range(n):
        m[x][y] = int(input())

for x in range(n - 1, -1, -1):
    p *= m[x][n - 1 - x]

print(f"O produto é: {p}")