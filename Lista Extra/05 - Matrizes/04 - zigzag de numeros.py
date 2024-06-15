'''
Escreva um programa que leia as dimensões de uma matriz e então imprima 
uma matriz que contém uma sequência de números ordenados linha a linha 
formando um zig-zag. Exemplo para uma matriz com 4 linhas e 3 colunas:

https://drive.google.com/file/d/1TT_iPnpUE5S1Tc8TdqtWRufu0AggcL9V/view?usp=drive_link

Entrada:

    L (número de linhas)
    C (número de colunas)

Exemplo:

3
5

Saída:

    Matriz com dimensões L x C com os múltiplos de 10 
    (em cada linha impressa, há um caractere espaço entre cada número impresso)

Exemplo:

1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
'''

l = int(input())
c = int(input())

m = [[((j * c) + i + 1) if j % 2 == 0 else ((j * c) + c - i) for i in range(c)]
     for j in range(l)]

for z in range(l):
    print(*m[z])