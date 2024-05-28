'''
Em matemática, o número harmônico designado por H(n) 
define-se como o enésimo termo da série harmônica. Ou seja:

H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n


Faça um programa, usando a estrutura de repetição for, 
que calcule o valor de qualquer H(n).

PS: O H(n) deve ser mostrado com para UMA casa decimal.

Os seguintes testes serão executados:

ENTRADA 1:

2

SAÍDA 1:

1.5

ENTRADA 2:

100

SAÍDA 2:

5.2
'''

N = int(input())
sum = 0.0

for x in range(N):
    sum += 1 / (x + 1)

print("{:.1f}".format(sum))