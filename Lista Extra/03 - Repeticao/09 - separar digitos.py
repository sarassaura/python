'''
Faça um programa que leia um valor inteiro N e então imprima em linhas separadas seus dígitos na ordem inversa. Por exemplo: O número 9376 seria impresso como:

6
7
3
9


Entrada:

    Valor inteiro N.

Saída:

    Dígitos do número, impressos linha a linha, em ordem inversa
'''

n = int(input())
m = str(n)

for x in m[::-1]:
    print(x)