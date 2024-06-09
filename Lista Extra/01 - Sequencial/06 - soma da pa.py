'''
Faça um programa que calcula a soma dos 
termos de uma Progressão Aritmética (PA) finita.
Seu programa irá receber o primeiro termo da 
progressão, a1, a razão da progressão, r, e o 
número de termos, n. Então, calcule e imprima 
a soma dos termos de a1 até an.

Relembre as fórmulas de progressão aritmética 
que serão úteis a esse exercício:

S = n*(a1 + an) / 2
an = a1 + (n − 1)*r

Observação: Não é permitido utilizar loops (for, while) 
e condicional (if) para resolver este exercício.

Entradas:

a1: Primeiro termo da PA (inteiro)
r: Razão (inteiro)
n: Número de termos (inteiro >0)

Saída:

S: Soma dos termos da PA (inteiro)

Exemplo:
Entradas:

1
1
3

Saída:

6

Exercício elaborado por Gabriel Ângelo Sembenelli (2022). 
'''

a1 = int(input())
r = int(input())
n = int(input())

an = a1 + (n - 1) * r
soma = n * (a1 + an) / 2

print(soma)