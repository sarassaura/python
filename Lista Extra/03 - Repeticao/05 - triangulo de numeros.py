'''
Faça um programa que leia um inteiro n e imprima um "triângulo" 
com os números. Por exemplo, para n=8, a saída seria:

1
22
333
4444
55555
666666
7777777
88888888


Entrada:

    Um número inteiro n.

Saída:

    Triângulo com os números.
'''

n = int(input())
total = 0

for x in range(n):
    for y in range(x + 1):
        print(x + 1, sep = "" ,end="")
    print()