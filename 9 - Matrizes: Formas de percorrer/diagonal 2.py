'''
Leia uma matriz de tamanho 3 × 3. Em seguida, imprima a soma dos valores
contidos em sua diagonal principal e também na sua diagonal secundária. 
Após isso, os elementos da matriz também devem ser impressos.

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Por exemplo,   

ENTRADAS 01:

12
2
34
0
9
10
1
4
2

SAÍDAS 01:

Soma diagonal principal: 23
Soma diagonal secundária: 44
12 2 34
0 9 10
1 4 2

ENTRADAS 02:

1
2
3
4
5
6
7
8
9

SAÍDAS 02:

Soma diagonal principal: 15
Soma diagonal secundária: 15
1 2 3
4 5 6
7 8 9

ENTRADAS 03:

0
9
8
-3
-4
-5
12
34
23

SAÍDAS 03:

Soma diagonal principal: 19
Soma diagonal secundária: 16
0 9 8 
-3 -4 -5
12 34 23
'''

m = [[0 for i in range(3)] for j in range(3)]

main = 0
sub = 0

for x in range(3):
    for y in range(3):
        m[x][y] = int(input())
        if x == y:
            main += m[x][y]
        if x + y == 2:
            sub += m[x][y]

print(f"Soma diagonal principal: {main}")
print(f"Soma diagonal secundária: {sub}")

for z in range(3):
    print(*m[z])