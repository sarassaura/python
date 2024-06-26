'''
Escreva um programa que leia um valor n e 
depois os n elementos de um vetor de inteiros.

Observação: após a leitura do valor n, os elementos 
do vetor estão todos dispostos em apenas uma linha. 
Por exemplo:

8
10 5 8 5 5 36 10 9

Para ler elementos em uma mesma linha em Python ou em Java, 
pode ser usada uma estratégia similar àquela apresentada 
no enunciado do 08 - Vetor crescente.

Depois imprima apenas a primeira ocorrência de cada número, 
ou seja, se um número aparece mais de uma vez no vetor, 
apenas a primeira ocorrência dele ser impressa.

Por exemplo, para o vetor [10, 5, 8, 5, 5, 36, 10, 9], 
o programa deve imprimir (nesta ordem):

10 5 8 36 9

Entrada:

    Comprimento do vetor (n);

    n inteiros

Saída:

    Primeira ocorrência de cada número no vetor lido
'''

n = int(input())

v = [0] * n

repeat = {}

result = ""

itens_linha = input().split(" ")
for i in range(n):
    v[i] = int(itens_linha[i])

    try:
        repeat[v[i]] += 1
    except:
        repeat[v[i]] = 1

for x in range(n):
    if repeat[v[x]] != 0:
        result += str(v[x]) + " "
        repeat[v[x]] = 0

print(result)