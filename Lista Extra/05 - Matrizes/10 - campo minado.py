'''
Escreva um programa que leia uma matriz que contém o mapa de um campo minado. 
Nesta matriz, o valor 1 indica que há uma bomba na célula e o valor 0 indica 
que não há uma bomba na célula. A matriz é composta apenas pelos valores 0 e 1. 
Exemplo de mapa do campo minado seguindo esse formato:

1 	1 	0 	0 	0 	1 	0
0 	0 	0 	1 	1 	0 	0
0 	1 	0 	0 	1 	1 	0
1 	0 	0 	0 	0 	1 	1
1 	1 	1 	0 	1 	0 	0

Observação: após a leitura das dimensões da matriz, os elementos de cada linha 
da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas 
são as dimensões da matriz: número de linhas (2) e número de colunas(3)):

2
3
1 0 1
0 0 1

Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui 
pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos 
dois primeiros exercícios sobre matrizes (01 e 02).

Após ler a matriz com o mapa, o programa irá ler as coordenadas de uma célula 
(linha e coluna) e então deverá imprimir quantas bombas há na vizinhança da célula 
(desconsiderando a própria célula). Por exemplo, para o mapa apresentado anteriormente, 
na célula (linha=2; coluna=3), há 3 bombas na vizinhança. 
Portanto, o programa deverá imprimir o valor 3 neste caso.

Importante: considere que os índices das linhas e colunas iniciam no zero. 
Portanto, a coluna 2 é a terceira coluna na matriz, 
assim como a linha 3 é a quarta linha na matriz.

Entrada

    Quantidade de linhas na matriz
    Quantidade de colunas na matriz
    Valores da matriz (mapa do campo minado)
    Linha da célula a ser consultada
    Coluna da célula a ser consultada

Saída

    Quantidade de bombas na vizinhança da célula
'''

l = int(input())
c = int(input())

m = [[0 for i in range(c)] for j in range(l)]

for lines in range(l):
    items = input().split(" ")
    for columns in range(c):
        m[lines][columns] = int(items[columns])

line = int(input())
column = int(input())

bombs = 0

for x in range(line-1, line+2):
    if x < 0:
        continue
    for y in range(column-1, column+2):
        if x == line and y == column:
            continue
        if y < 0:
            continue
        try:
            cell = m[x][y]
            if cell == 1:
                bombs += 1
        except:
            cell = 0

print(bombs)