'''
Faça um programa que leia dois números inteiros x e y, 
com y > x, e crie um vetor de inteiros chamado vec, 
com todos os valores no intervalo [x, y].

Depois, mostre o vetor criado. 
Para mostrar o vetor você pode usar o comando print(*v), 
que automaticamente mostra os elementos contidos em v.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, sort, in, reverse, index, count, etc.

Alguns testes que serão executados:

ENTRADAS 01:

1
3

SAÍDA 01:

1 2 3


ENTRADAS 02:

5
10

SAÍDA 02:

5 6 7 8 9 10
'''

x = int(input())
y = int(input())

vec = []

while y >= x:
    vec.append(x)
    x += 1

print(*vec)