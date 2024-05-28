'''
Escreva um programa que leia um valor n e um valor x. 
Depois, crie uma matriz de dimensões n x n 
com valores sequenciais iniciando em x, 
linha após linha e coluna após coluna. 

Depois, mostre a matriz transposta 
(invertendo linhas e colunas) daquela que foi criada. 
Ao mostrar a matriz, os valores devem 
ser impressos com um caractere espaço entre os elementos.

Por exemplo, para n = 3 e x = 4, a matriz criada será:

4 5 6
7 8 9
10 11 12

E a matriz transposta a ser mostrada será:

4 7 10 
5 8 11 
6 9 12

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, numpy, arange etc.
'''

n = int(input())
p = int(input())

m = [[p for i in range(n)] for j in range(n)]

for x in range(n):
    for y in range(n):
        m[x][y] += (n * x) + y

i = 0
j = 0

while i < n - 1:
    j = i + 1
    while j < n:
        temp = m[i][j]
        m[i][j] = m[j][i]
        m[j][i] = temp
        j += 1
    i += 1

for z in range(n):
    print(*m[z])