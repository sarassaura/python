'''
Escreva um programa que leia duas matrizes: A e B. 
Depois mostre o resultado da seguinte operação: 3 x A x B.

Observação: após a leitura das dimensões de uma matriz, 
os elementos de cada linha da matriz estão dispostos linha por linha. 
Por exemplo (as duas primeiras linhas são as dimensões da matriz: 
número de linhas (2) e número de colunas(3)):

2
3
5 6 2
7 2 1

Dica para Python ou Java: a leitura dos elementos das matrizes da forma 
descrita aqui pode ser realizada com uma estratégia similar àquela apresentada 
no enunciado dos dois primeiros exercícios sobre matrizes (01 e 02).

Entrada:

    Número de linhas da matriz A
    Número de colunas da matriz A
    Elementos da matriz A
    Número de linhas da matriz B
    Número de colunas da matriz B
    Elementos da matriz B

Saída:

    Matriz resultado da operação 3 x A x B, isto é, o escalar 3 que multiplica a matriz AxB.
'''

a_lines = int(input())
a_columns = int(input())

a = [[0 for i in range(a_columns)] for j in range(a_lines)]

for lines in range(a_lines):
    items = input().split(" ")
    for columns in range(a_columns):
        a[lines][columns] = int(items[columns])

b_lines = int(input())
b_columns = int(input())

b = [[0 for i in range(b_columns)] for j in range(b_lines)]

for lines in range(b_lines):
    items = input().split(" ")
    for columns in range(b_columns):
        b[lines][columns] = int(items[columns])

c = [[0 for i in range(b_columns)] for j in range(a_lines)]

for x in range(a_lines):
    for y in range(b_columns):
        soma = 0
        for z in range(a_columns):
            soma += a[x][z] * b[z][y]
        c[x][y] = 3 * soma

for z in range(a_lines):
    print(*c[z])