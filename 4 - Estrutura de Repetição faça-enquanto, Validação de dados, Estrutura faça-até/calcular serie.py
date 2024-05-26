'''
Faça um programa, usando a estrutura de repetição for, 
que leia n e mostre o valor S que é calculado da seguinte forma:

S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m

O valor de S deve ser mostrado com DUAS casas decimais.

Os seguintes testes serão executados:

ENTRADA 1:

2

SAÍDA 1:

1.67

ENTRADA 2:

5

SAÍDA 2:

3.39

ENTRADA 3:

9

SAÍDA 3:

5.54
'''

N = int(input())
sum = 0.0

for x in range(N):
    sum += (x + 1) / ((x * 2) + 1)

print("{:.2f}".format(sum))