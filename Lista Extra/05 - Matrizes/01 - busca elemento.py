'''
Faça um programa que busque um número específico dentro de uma matriz.
O tamanho da matriz será definido pelo usuário, que vai entrar com a 
quantidade de linhas e depois com a quantidade de colunas. Após isso, 
o usuário vai inserir cada um dos elementos da matriz e, ao final, 
vai inserir qual é o número a ser buscado 
(é garantido que o número buscado aparece no máximo uma vez na matriz). 
Ao final, o programa deverá imprimir a posição do número buscado, ou seja, 
o número da linha e o número da coluna em que se encontra 
(note que o índice [0][0] no programa corresponde à posição da linha=1 e coluna=1). 
Caso o número não exista na matriz, imprima apenas o número -1.


Entradas:

    Número de linhas da matriz (inteiro >0)
    Número de colunas da matriz (inteiro >0)
    Elementos que compõem a matriz (inteiros)
    Número a ser buscado na matriz (inteiro)

Saídas:

    Posição do número buscado (ou -1 caso não exista)



Observações:
1. Nos exemplos, temos a matriz 2x3 abaixo. No primeiro exemplo, 
buscamos o elemento 4, que está na posição a21. No segundo exemplo, 
buscamos o elemento 8, que não existe nessa matriz.

   1 2 3
   4 5 6

Exemplo 1:
Entradas:

2
3
1
2
3
4
5
6
4

Saídas:

2 1


Exemplo 2:
Entradas:

2
3
1
2
3
4
5
6
8

Saídas:

-1

Exercício elaborado por Gabriel Ângelo Sembenelli (2022).
'''

l = int(input())
c = int(input())

m = [[0 for i in range(c)] for j in range(l)]

for x in range(l):
    for y in range(c):
        m[x][y] = int(input())

n = int(input())

line = -1
column = -1

for x in range(l):
    for y in range(c):
        if m[x][y] == n:
            line = x
            column = y

if line != -1:
    print(f"{line + 1} {column + 1}")
else:
    print(-1)