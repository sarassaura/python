'''
Faça um programa que leia um número inteiro n, 
crie e mostre uma matriz n x n com elementos booleanos 
em que apenas a moldura tenha valor True 
(os outros elementos são False). Veja os exemplos de saída. 

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Desafio: Você consegue usar compreensão de listas e criar a matriz, 
conforme requerida, usando apenas uma linha de código?

Exemplo de Entrada 1:
3

Saída 1:

TrueTrue True
True False True
True True True


Exemplo de Entrada 2:
4

Saída 2:

True True True True
True False False True
True False False True
True True True True
'''

n = int(input())

m = [[True if i == 0 or j == 0 or i == (
    n-1) or j == (n - 1) else False for i in range(n)] for j in range(n)]

for x in range(n):
    print(*m[x])