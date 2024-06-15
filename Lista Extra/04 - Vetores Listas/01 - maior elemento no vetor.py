'''
Escreva um programa para ler um vetor de inteiros com n elementos. 
O valor n deve ser fornecido em tempo de execução. Retorne o maior elemento do vetor.

Entrada:

    Um valor n;
    n valores inteiros.

Saída:

    O maior valor no vetor lido.
'''

n = int(input())
vec = []
maior = float("-inf")

for x in range(n):
    y = int(input())
    vec.append(y)

    if y > maior:
        maior = y

print(maior)