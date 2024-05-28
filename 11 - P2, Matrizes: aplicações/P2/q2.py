'''
Escreva um programa que leia um valor n, 
os elementos (linha a linha) de uma matriz de inteiros com 
dimensões n x n, e os índices (linha e coluna) de 
uma determinada célula da matriz. Depois, deve-se 
imprimir a soma dos elementos localizados na linha e 
também na coluna, com exceção da própria célula. 
Por exemplo, para a seguinte matriz, linha = 1 e coluna = 5:  

9 	1 	5 	0 	0 	1 	3
7 	8 	0 	1 	5 	4 	5
0 	1 	7 	0 	1 	6 	7
1 	0 	6 	0 	0 	1 	1
1 	1 	1 	0 	1 	4 	2
3 	4 	7 	0 	2 	3 	1
1 	3 	8 	9 	0 	5 	3

A soma dos elementos da linha=1 é 7 + 8 + 0 + 1 + 5 + 5 = 26 e 
da coluna=5 é 1 + 6 + 1 + 4 + 3 + 5 = 20. 
Vale ressaltar que o elemento 4 (linha=1 e coluna=5) 
não foi considerado no cálculo. Portanto, neste exemplo, 
as seguintes informações devem ser impressas:

soma linha = 26
soma coluna = 20

9 1 5 0 0 1 3
7 8 0 1 5 4 5
0 1 7 0 1 6 7
1 0 6 0 0 1 1
1 1 1 0 1 4 2
3 4 7 0 2 3 1
1 3 8 9 0 5 3

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, sort, reverse, index, count, etc.

Alguns testes que serão realizados:

ENTRADAS 1

3
50
10
20
50
99
10
80
20
30
1
1

SAÍDAS 1

soma linha = 60
soma coluna = 30
50 10 20 
50 99 10 
80 20 30
ENTRADAS 2

3
50
10
20
50
99
10
80
20
30
0
2

SAÍDAS 2

soma linha = 60
soma coluna = 40
50 10 20 
50 99 10 
80 20 30
'''

n = int(input())
m = [[0 for i in range(n)] for j in range(n)]

for x in range(n):
  for y in range(n):
    m[x][y] = int(input())

line = int(input())
column = int(input())

soma_linha = 0
soma_coluna = 0

replace = m[line][column]
m[line][column] = 0

for z in range(n):
  soma_linha += m[line][z]
  soma_coluna += m[z][column]

print(f"soma linha = {soma_linha}")
print(f"soma coluna = {soma_coluna}")

m[line][column] = replace

for x in range(n):
  print(*m[x])