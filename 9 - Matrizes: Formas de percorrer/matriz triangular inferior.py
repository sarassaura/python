'''
Escreva um programa que leia um valor n e 
depois os elementos de uma matriz A com dimensão n x n. 
Após isso, seu programa deve transformar a matriz A em 
uma matriz triangular inferior 
(com elementos apenas abaixo da diagonal principal) 
e mostrá-la. 

Por exemplo, para n = 3, e matriz A a seguir:

1 2 3
4 5 6
7 8 9

A matriz a ser impressa, será:

0 0 0
4 0 0
7 8 0

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, numpy, arange etc.
'''

n = int(input())

a = [[0 for i in range(n)] for j in range(n)]

for x in range(n):
    for y in range(n):
        a[x][y] = int(input())

x = 0
y = 0

while x < n:
    y = x
    while y < n:
        a[x][y] = 0
        y += 1
    x += 1

for z in range(n):
    print(*a[z])
