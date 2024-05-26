'''
Faça um programa, usando a estrutura de repetição for, 
que peça dois números inteiros positivos, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 

Não utilize a função de potência do Python (** ou pow).

Os seguintes testes serão executados:

ENTRADA 1:

2
3

SAÍDA 1:

8

ENTRADA 2:

3
8

SAÍDA 2:

6561
'''

A = int(input())
B = int(input())
res = 1

for x in range(B):
    res = res * A

print(res)