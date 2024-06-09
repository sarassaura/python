'''
Faça um programa que leia um número real x e 
crie um vetor de números reais chamado vec com 
6 elementos começando em x e terminando em x + 0.5.

Depois, mostre o vetor criado e 
a soma dos elementos nas extremidades do vetor. 
Para mostrar o vetor você pode usar o comando print(*v), 
que automaticamente mostra os elementos contidos em v.

Dica: use o comando linspace da biblioteca numpy.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, sort, in, reverse, index, count, etc.

Alguns testes que serão executados:

ENTRADAS 01:

1

SAÍDA 01:

1.0 1.1 1.2 1.3 1.4 1.5
2.5
'''

x = float(input())

vec = []

for y in range(6):
    vec.append(x + (y * 0.1))

print(*vec)
print(x + vec[5])