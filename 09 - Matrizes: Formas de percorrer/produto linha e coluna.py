'''
Escreva um programa que leia um valor n e 
depois os elementos de uma matriz A com dimensão n x n. 
Após isso, seu programa deve criar uma outra matriz B 
com dimensão n x n, em que os elementos de A são 
multiplicados por 3 caso o índice da linha seja par e 
multiplicados por -2 caso o índice da linha seja ímpar. 
Após esse processamento a matriz B deve ser impressa.

Por exemplo, para n = 3, e matriz A a seguir:

1 2 3
4 5 6
7 8 9

A matriz B, a ser impressa, será:

3 6 9
-8 -10 -12
21 24 27

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, numpy, arange etc.
'''

n = int(input())

a = [[0 for i in range(n)] for j in range(n)]

for x in range(n):
    for y in range(n):
        a[x][y] = int(input())

b = [[(a[j][i] * 3) if (j % 2) == 0 else (a[j][i]
      * -2) for i in range(n)] for j in range(n)]

for z in range(n):
    print(*b[z])