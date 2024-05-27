'''
Faça um programa que LEIA um valor inteiro e positivo N, 
calcule o mostre o valor E, conforme a fórmula a seguir:

E = 1/1! + 1/2! + 1/3! + ... + 1/N!

O valor de E deve ser mostrado com três casas decimais. 

Os seguintes testes serão executados:

ENTRADA 1:

7

SAÍDA 1:

1.718

ENTRADA 2:

2

SAÍDA 2:

1.500
'''

def calculate(N):
    X = 1
    for id in range(N):
        X = X * (N - id)
    return X

A = int(input())
sum = 0

for x in range(A):
    sum += 1 / calculate(x + 1)

print("{:.3f}".format(sum))