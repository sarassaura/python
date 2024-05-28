'''
Implemente um algoritmo que leia do teclado SEIS valores inteiros e 
em seguida mostre na tela os valores lidos na ORDEM INVERSA.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Alguns testes que serão executados:

ENTRADAS 01:

1
2
3
4
5
6

SAÍDAS 01:

6 5 4 3 2 1


ENTRADAS 02:

6
5
4
3
2
1

SAÍDAS 02:

1 2 3 4 5 6
'''

vec = [0] * 6

for x in range(6):
    vec[x] = int(input())

for x in range(6):
    print(vec[5- x], end=' ')