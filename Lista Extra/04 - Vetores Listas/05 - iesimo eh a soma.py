'''
Faça um programa que verifique se o elemento em um dado índice de 
um vetor é igual à soma de todos os outros elementos desse vetor.

Seu programa irá receber o tamanho do vetor. Em seguida, receberá 
todos os elementos que compõem esse vetor (inteiros). Ao final, seu 
programa irá receber um índice e deverá verificar se o número armazenado 
nesse índice é igual à soma de todos os outros. Imprima "Sim" em caso 
afirmativo ou "Nao" caso contrário.

Observações:
O primeiro elemento de um vetor está no índice 0

Entradas:

    Tamanho do vetor (inteiro >0

    )
    Elementos do vetor (inteiros)
    Índice de interesse (inteiro entre 0 e o tamanho do vetor)

Saídas:

    "Sim" caso o elemento do índice seja a soma dos outros elementos
    "Nao" caso contrário


Exemplo 1:
Entradas:

3
1
2
3
2

Saídas:

Sim


Exemplo 2:
Entradas:

4
-1
4
2
2
1

Saídas:

Nao

Exercício elaborado por Gabriel Ângelo Sembenelli (2022).
'''

size = int(input())
vec = []
sum = 0

for x in range(size):
    vec.append(int(input()))

id = int(input())

all = vec[id]

for x in range(size):
    if x != id:
        sum += vec[x]

if sum == all:
    print("Sim")
else:
    print("Nao")