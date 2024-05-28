'''
Faça um programa que permita ao usuário entrar com uma matriz 
de tamanho 3 × 3 de números INTEIROS. Em seguida, 
calcule um VETOR contendo TRÊS posições, 
em que cada posição deverá armazenar a SOMA dos números 
de cada COLUNA da matriz. Exiba na tela esse array. 
Por exemplo, a matriz

5 −8 10
1 2 15
25 10 7

deverá gerar o vetor

31 4 32

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Os seguintes testes serão realizados no seu algoritmo:   

ENTRADAS 01:

5
-8
10
1
2
15
25
10
7

SAÍDA 01:

31 4 32

ENTRADAS 02:

1
1
1
1
1
1
1
1
1

SAÍDA 02:

3 3 3

ENTRADAS 03:

3
2
4
5
6
9
0
1
2

SAÍDA 03:

8 9 15
'''

m = [[0 for i in range(3)] for j in range(3)]

soma = [0] * 3

for x in range(3):
    for y in range(3):
        m[x][y] = int(input())
        soma[y] += m[x][y]

for z in range(3):
    print(soma[z], sep=' ', end=' ')