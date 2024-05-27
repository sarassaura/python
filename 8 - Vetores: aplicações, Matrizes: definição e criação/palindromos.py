'''
Faça um programa que teste se uma palavra ou número é um palíndromo. 
Se uma palavra pode ser lida, indiferentemente, 
da esquerda para a direita e vice-versa, 
ela é considerada um palíndromo. 
Mesma coisa com um número.

Você deve passar a palavra ou o número a ser testado. 
O seu programa deverá imprimir as seguintes mensagens 
“É um palíndromo” (caso seja um palíndromo) ou 
“Não é um palíndromo” (caso não seja um palíndromo).

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

a = input()
inv = []
valid = True

for x in range(len(a)):
    inv.append(a[x])

for y in range(len(a)):
    if inv[y] != inv[len(a) - 1 - y]:
        valid = False

if valid:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")