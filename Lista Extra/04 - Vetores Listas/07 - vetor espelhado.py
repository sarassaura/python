'''
Escreva um programa que leia um vetor de inteiros com n elementos. 
Depois verifique se o vetor é "espelhado", ou seja, 
a primeira metade é igual ao inverso da segunda. Por exemplo, 
os vetores a seguir são "espelhados": 
[5 9 7 8 8 7 9 5], [1 2 3 2 1], mas o vetor [1 2 3 4 5] não é.

Entrada:

    Um valor n (0 <= n <= 50);

    n inteiros

Saída:

    Imprima "SIM" se o vetor for "espelhado" e "NAO" caso contrário.
'''

n = int(input())
vec = []
yes = True

for x in range(n):
    vec.append(int(input()))

for x in range(n):
    if vec[x] != vec[n-x-1]:
        print("NAO")
        yes = False
        break

if yes == True:
    print("SIM")