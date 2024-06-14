'''
Faça um programa que leia um valor inteiro N e então 
mostre os N primeiros números primos 
(o primeiro número primo é o 2).

Entrada:

    Valor inteiro N.

Exemplo:

5

Saída:

    N primeiros números primos.

Exemplo:

2
3
5
7
11
'''

n = int(input())
now = 3
primos = []
itsnot = True

print(2)
    
while len(primos) + 1 < n:

    for x in primos:
        if now % x == 0:
            itsnot = False

    if itsnot == True:
        primos.append(now)
        print(now)

    now += 2
    itsnot = True