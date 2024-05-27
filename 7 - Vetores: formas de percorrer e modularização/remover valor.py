'''
Escreva um programa que:

    Leia um valor inteiro n, depois leia os n valores de um vetor.
    Imprima os elementos do vetor lido (separe cada elemento por um caractere espaço).
    Após isso, leia um índice i e remova o elemento na posição i do vetor. 
    Neste exercício, para remover um elemento, 
    desloque uma posição para a esquerda os elementos que vem depois do índice removido 
    (inclua um valor -1 na última posição do vetor). 
    Exemplo: remover o elemento no índice 3 do vetor [11, 55, 66, 99, 33, 22, 77, 88]. 
    Após a remoção: [11, 55, 66, 33, 22, 77, 88, -1].
    Imprima os elementos do vetor após a remoção 
    (separe cada elemento por um caractere espaço).

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, pop, remove, etc.
'''

n = int(input())
vec = [0] * n

for x in range(n):
    vec[x] = int(input())

for x in range(n):
    print(vec[x], end=' ')


print()
i = int(input())

for x in range(i, n - 1):
    vec[x] = vec[x + 1]

vec[len(vec) - 1] = -1

for x in range(n):
    print(vec[x], end=' ')