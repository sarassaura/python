'''
Escreva um programa que leia um número inteiro positivo n e 
em seguida imprima n linhas do chamado Triângulo de Pascal, 
conforme o exemplo para n = 6.

1
1  1
1  2  1
1  3  3  1
1  4  6  4  1
1  5  10 10 5 1

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

n = int(input())
  
for i in range(1, n+1): 
    C = 1
    for j in range(1, i+1): 
        print(' ', C, sep='', end='') 
        C = C * (i - j) // j
    print() 