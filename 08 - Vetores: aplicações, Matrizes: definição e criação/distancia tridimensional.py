'''
Faça um programa que leia dois vetores a e b com 3 elementos reais cada, 
que representam um ponto no espaço tridimensional 
(cada elemento dos vetores é o valor de uma coordenada espacial). 
Os vetores devem ser lidos sequencialmente, isto é, 
primeiro lê-se o vetor a e depois o vetor b. 
Seu programa deve calcular a distância (d) 
entre estes dois pontos usando a fórmula:

d = ((ax−bx)^2 + (ay−by)^2 + (az−bz)^2)^(0.5)

A saída do programa será: 
"A distância entre os dois pontos é d.", 
em que d deve ser formatado com 2 casas decimais.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

a = [0] * 3
b = [0] * 3
d = 0

for x in range(3):
    a[x] = float(input())

for x in range(3):
    b[x] = float(input())

for x in range(3):
    d += (a[x] - b[x])**2

d = d**0.5

print("A distância entre os dois pontos é {:.2f}.".format(d))