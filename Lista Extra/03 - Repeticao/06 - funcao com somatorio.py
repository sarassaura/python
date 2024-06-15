'''
Faça um programa que leia um valor inteiro n e então 
calcule o valor de f( n ), conforme definição a seguir:

f(n)=∑(n,i=1) ∑(8,j=1) (i + 1)*j

Entrada:

    Valor inteiro n.

Saída:

    Valor de f(n).
'''

n = int(input())

sum = 0

for x in range(n):
    for y in range(8):
        sum += ((x + 1) + 1) * (y + 1)

print(sum)