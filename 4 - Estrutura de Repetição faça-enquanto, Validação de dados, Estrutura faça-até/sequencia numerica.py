'''
Faça um programa, usando a estrutura de repetição for, 
que leia dois números inteiros N e s 
e mostre uma sequência começando em N, 
cujos elementos sucessivos sejam decrementados de s, 
até que o último número seja maior ou igual a zero.

Exemplo de execução:

ENTRADAS:

10
3


SAÍDA:

10 7 4 1
'''

N = int(input())
S = int(input())

for x in range(N,0,-S):
    
    print(x, end = ' ')

    if x - S == 0:
        print(0, end = '')