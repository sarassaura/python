'''
Faça um programa que LEIA do TECLADO um vetor de 
10 posições e escreva na tela os números PARES e ÍMPARES. 
É importante destacar que o seu algoritmo NÃO deve imprimir, 
caso tiver, números PARES e ÍMPARES repetidos. 
Além disso, o MAIOR e MENOR número também deve ser impresso.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Para este exercício, os seguintes testes serão executados:

ENTRADAS 1:

2
4
5
3
1
7
6
5
4
3

SAÍDAS 1:

Números pares:
2
4
6
Números impares:
5
3
1
7
Maior: 7
Menor: 1

ENTRADAS 2:

0
1
2
3
4
5
6
7
8
9

SAÍDAS 2:

Números pares:
0
2
4
6
8
Números impares:
1
3
5
7
9
Maior: 9
Menor: 0

ENTRADAS 3:

2
2
4
4
6
6
6
8
8
8

SAÍDAS 3:

Números pares:
2
4
6
8
Números impares:
Maior: 8
Menor: 2
'''

vec = [0] * 10
odd = []
even = []
big = float("-inf")
small = float("inf")
repeated = {}

for x in range(10):
    y = int(input())

    vec[x] = y

    try:
        repeated[y] += 1
    except:
        repeated[y] = 1

    if y % 2 == 0:
        even.append(y)
    else:
        odd.append(y)

    if y > big:
        big = y

    if y < small:
        small = y

print("Números pares:")

for x in range(len(even)):
    if repeated[even[x]] != 0:
        print(even[x])
        repeated[even[x]] = 0

print("Números ímpares:")

for x in range(len(odd)):
    if repeated[odd[x]] != 0:
        print(odd[x])
        repeated[odd[x]] = 0

print("Maior: {:d}".format(big))
print("Menor: {:d}".format(small))