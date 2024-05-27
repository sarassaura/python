'''
Faça um programa que receba do usuário DOIS arrays, 
A e B, com 5 números inteiros cada. 
Crie um novo array C calculando C = A - B. 
Mostre na tela os dados do array C.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Os seguintes testes serão executados:

ENTRADAS 1:

1 
2
3
7
1
3
4
2
3
9

SAÍDA 1:

-2 -2 1 4 -8

ENTRADAS 02:

3
2
1
4
3
0
9
2
6
5

SAÍDA 2:

3 -7 -1 -2 -2

ENTRADAS 03:

-1
-3
-5
2
8
9
-4
-2
1
0

SAÍDAS 3:

-10 1 -3 1 8
'''

A = [0] * 5
B = [0] * 5
C = [0] * 5

for x in range(5):
    A[x] = int(input())

for x in range(5):
    B[x] = int(input())

for x in range(5):
    C[x] = A[x] - B[x]

for x in range(5):
    print(C[x], end=' ')