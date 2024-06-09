'''
Faça um programa, usando a estrutura de repetição for, 
que leia 10 valores e imprima na tela quantos estão entre 
0 e 10, 11 e 20 e maiores de 21. 
Formate a saída de seu programa de acordo com os três testes:

>=0 e <=10: x
>=11 e <=20: y
>=21: z

em que x, y e z são os números valores em cada intervalo.

Os seguintes testes serão executados:

ENTRADAS 1:

1
2
3
4
5
6
7
8
9
10

SAÍDAS 1:

>=0 e <=10: 10
>=11 e <=20: 0
>=21: 0

ENTRADAS 2:

8
12
99
10
2
3
15
2
65
45

SAÍDAS 2:

>=0 e <=10: 5
>=11 e <=20: 2
>=21: 3
'''

X = 0
Y = 0
Z = 0

for N in range(10):
    number = int(input())

    if number >= 0 and number <= 10:
        X += 1
    elif number >= 11 and number <= 20:
        Y += 1
    elif number > 20:
        Z += 1

print(">=0 e <=10: {:d}".format(X))
print(">=11 e <=20: {:d}".format(Y))
print(">=21: {:d}".format(Z))