'''
Escreva um programa que leia uma matriz com dimensões n x n. 
Depois, calcule a soma de todos os valores pares abaixo da diagonal principal.

Para ler a matriz, primeiro será informada a dimensão n. 
Após isso, os elementos de cada linha da matriz estão dispostos linha por linha. 
Por exemplo (a primeira linha é o valor de n):

3
6 3 2
7 8 9
2 8 1

Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui 
pode ser realizada com uma estratégia similar àquela apresentada no enunciado no 
02 - Média dos alunos.

Entrada:

    n
    Dados da matriz

Exemplo:

3
6 3 2
7 8 9
2 8 1

Saída:

    Soma dos valores pares abaixo da diagonal principal.

Exemplo:

10
'''

n = int(input())

m = [[0 for i in range(n)] for j in range(n)]

for line in range(n):
    items = input().split(" ")
    for column in range(n):
        m[line][column] = int(items[column])

x = 1
soma = 0

while x < n:
    y = 0
    while y < x:
        if m[x][y] % 2 == 0:
            soma += m[x][y]
        y += 1
    x += 1

print(soma)