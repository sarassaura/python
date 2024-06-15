'''
Escreva um programa que leia um vetor de inteiros com n elementos. 
Depois some todos os valores que são vizinhos aos elementos com valor 1.

Por exemplo, para o vetor [12, 1, 50, 60, 70, 1], o programa deve imprimir 132, 
que é o resultado da soma 12 + 50 + 70 
(os valores vizinhos aos elementos com valor 1 no vetor.

Entrada:

    Um valor n (quantidade de elemento do vetor);

    n inteiros

Saída:

    Somatório dos valores vizinhos aos elementos com valor 1
'''

n = int(input())
vec = []
sum = 0

for x in range(n):
    vec.append(int(input()))

vec.append(0)

for x in range(n + 1):
    if vec[x] == 1:
        sum += vec[x + 1]
        sum += vec[x - 1]

print(sum)