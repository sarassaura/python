'''
Implemente um algoritmo que leia uma matriz (inteiros) 
de tamanho 3 × 3 com números diferentes. 
Imprima na tela o menor valor e o maior valor contido nessa matriz, 
assim como a sua localização (linha e coluna). 
Após isso, os elementos da matriz também devem ser impressos.

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Por exemplo,   

ENTRADAS 01:

1
2
3
4
5
6
7
8
9

SAÍDAS 01:

Maior: 9
Posição (maior): 2 linha e 2 coluna
Menor: 1
Posição (menor): 0 linha e 0 coluna
1 2 3 
4 5 6
7 8 9
'''

m = [[0 for i in range(3)] for j in range(3)]
maior = [[0] for j in range(3)]
menor = [[0] for j in range(3)]

maior[0] = float('-inf')
menor[0] = float('inf')

for x in range(3):
    for y in range(3):
        m[x][y] = int(input())
        if m[x][y] > maior[0]:
            maior[0] = m[x][y]
            maior[1] = x
            maior[2] = y
        if m[x][y] < menor[0]:
            menor[0] = m[x][y]
            menor[1] = x
            menor[2] = y

print(f"Maior: {maior[0]}")
print(f"Posição (maior): {maior[1]} linha e {maior[2]} coluna")
print(f"Menor: {menor[0]}")
print(f"Posição (menor): {menor[1]} linha e {menor[2]} coluna")

for z in range(3):
    print(*m[z])