'''
Faça um programa que leia dois números inteiros L e C e 
crie uma matriz L x C contendo apenas círculos ('o'). 
Depois, seu programa deve ler dois índices inteiros l e c, 
setar o valor da matriz nesses índices para 'x' e mostrá-la. veja o exemplo 

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Exemplo de Entrada 1:
2
2
1
1

Saída 1:
o o
o x

Exemplo de Entrada 2:
3
4
2
1

Saída 2:
o o o o
o o o o
o x o o
'''

L = int(input())
C = int(input())

m = [['o' for i in range(C)] for j in range(L)]

l = int(input())
c = int(input())

m[l][c] = 'x'

for x in range(L):
    print(*m[x])