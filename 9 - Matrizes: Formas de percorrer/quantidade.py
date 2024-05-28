'''
Leia uma matriz de tamanho 4 × 4. Em seguida, CONTE e ESCREVA 
na tela a quantidade de valores MAIORES do que 10 e 
também a quantidade de números NEGATIVOS. 
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
1
2
3
4
5
6
7

SAÍDAS 01:

Maior que 10: 0
Menor que 0: 0
1 2 3 4
5  6 7 8
9 1 2  3
4 5 6 7

ENTRADAS 02:

4
-2
-3
56
-9
-5
12
32
1
2
3
4
32
98
8
7

SAÍDAS 02:

Maior que 10: 5
Menor que 0: 4
4 -2 -3 56
-9  -5 12 32
1 2 3  4
32 98 8 7

ENTRADAS 03:

-2
-3
4
-5
-1
2
3
4
5
6
7
2
9
8
0
0

SAÍDAS 03:

Maior que 10: 0
Menor que 0: 4
-2 -3 4 -5
-1 2 3 4
5 6 7 2
9 8 0 0
'''

m = [[0 for i in range(4)] for j in range(4)]

dezmais = 0
negative = 0

for x in range(4):
    for y in range(4):
        m[x][y] = int(input())
        if m[x][y] > 10:
            dezmais += 1
        if m[x][y] < 0:
            negative += 1

print(f"Maior que 10: {dezmais}")
print(f"Menor que 0: {negative}")

for z in range(4):
    print(*m[z])