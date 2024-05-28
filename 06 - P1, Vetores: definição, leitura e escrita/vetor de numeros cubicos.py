'''
Faça um programa que leia um número inteiro x e 
crie um vetor de inteiros chamado vec, 
contendo 7 posições, 
cujos elementos são os primeiros 
números cúbicos começando em x^3.

Depois, mostre o vetor criado. 
Para mostrar o vetor você pode usar o comando print(*v), 
que automaticamente mostra os elementos contidos em v.

Para resolver este problema, 
uma dica é usar compreensão de listas.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, sort, in, reverse, index, count, etc.

Alguns testes que serão executados:

ENTRADAS 01:

5

SAÍDA 01:

125 216 343 512 729 1000 1331
'''

x = int(input())

vec = []

for y in range(7):
    vec.append(x**3)
    x += 1

print(*vec)