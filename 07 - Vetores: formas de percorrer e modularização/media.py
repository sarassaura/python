'''
Implemente um algoritmo que leia cinco valores e 
armazene-os em um vetor. Em seguida, 
mostre todos os valores lidos 
juntamente com a média dos valores.

Ps: A média deve ser mostrada usando DUAS casas decimais.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Para este exercício, os seguintes testes serão executados:

ENTRADAS 1:

7
4
3
2
1

SAÍDAS 1:

7 4 3 2 1
3.40

ENTRADAS 2:

5
4
37
8
6

SAÍDAS 2:

5 4 37 8 6
12.00
'''

vec = [0] * 5
media = 0

for x in range(5):
    vec[x] = int(input())
    media += vec[x] / 5

for x in range(5):
    print(vec[x], end=' ')

print()
print("{:.2f}".format(media))