'''
Escreva um programa que leia uma matriz de dimensões n x n (assuma que n é par). 
Após isso, imprima o resultado da matriz dobrada da seguinte forma:

https://drive.google.com/file/d/1lg_6UvWURVdAV9u4cmBQyIfWez1JGQJI/view?usp=drive_link

Para ler a matriz, primeiro será informada a dimensão n. Após isso, 
os elementos de cada linha da matriz estão dispostos linha por linha. 
Por exemplo (a primeira linha é o valor de n):

3
6 3 2
7 8 9
2 8 1

Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui 
pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos 
dois primeiros exercícios sobre matrizes (01 e 02).

Entrada:

    n
    Dados da matriz

Saída:

    Matriz após as dobras
'''

n = int(input())

m = [[0 for i in range(n)] for j in range(n)]

for line in range(n):
    items = input().split(" ")
    for column in range(n):
        m[line][column] = int(items[column])

for x in range(n):
    for y in range(n // 2):
        m[x][y] += m[x][n - 1 - y]

for x in range(n // 2):
    for y in range(n // 2):
        m[x][y] += m[n - 1 - x][y]

for x in range(n // 2):
    for y in range(n // 2):
        print(m[x][y], sep=' ', end=' ')
    print()