'''
Implemente um algoritmo que leia três inteiros e 
imprima o maior número, se todos os valores forem iguais 
imprimir a mensagem "Numeros Iguais!".

Alguns testes que serão realizados:

ENTRADAS 1:

1
2
3

SAÍDA 1:

Maior eh: 3

ENTRADAS 2:

3
2
1

SAÍDA 2:

Maior eh: 3

ENTRADAS 3:

2
3
1

SAÍDA 3:

Maior eh: 3

ENTRADAS 4:

2
2
2

SAÍDA 4:

Numeros Iguais!
'''

A = int(input())
B = int(input())
C = int(input())

maior = A

if A == B == C:
    print("Numeros Iguais!")
else:
    if B > maior:
        maior = B

    if C > maior:
        maior = C

    print("Maior eh:", maior)