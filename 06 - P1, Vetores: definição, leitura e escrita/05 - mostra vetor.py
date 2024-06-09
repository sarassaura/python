'''
Faça um programa que lê 5 números inteiros, 
armazene-os em um vetor chamado vec, 
e em seguida mostre os valores contidos nesse vetor.

Dica: use um laço de repetição para ler os valores a serem acrescentados no vetor.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, sort, in, reverse, index, count, etc.

Alguns testes que serão executados:

ENTRADAS 01:

1
2
3
4
5

SAÍDAS 01:

1 2 3 4 5


ENTRADAS 02:

3
5
8
10
11

SAÍDAS 02:

3 5 8 10 11
'''

vec = []

for x in range(5):
    y = int(input())
    vec.append(y)

print(*vec)