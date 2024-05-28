'''
Um professor calcula a nota do curso (N) da seguinte forma:

N = 0,3 x P1 + 0,5 x P2 + 0,2 x MEPP + 0,05 x ML

Neste cálculo, P1 é a nota da Prava 1, P2 é a nota da Prova 2, 
MEPP é a média das notas das atividades práticas e 
ML é a média obtida com exercícios extras (usados para bônus).

Escreva um programa que leia as notas P1, P2, MEPP, e ML. 
Após isso, imprima o valor de N.

Observação: imprima o valor usando duas casas decimais. 
Para formatar a saída em Python é possível utilizar o seguinte código:

numero = 5.07507
print("Valor = {:.2f}".format(numero))


Entrada:

    P1
    P2
    MEPP
    ML

Saída:

    N
'''

p1 = float(input())
p2 = float(input())
mepp = float(input())
ml = float(input())

n = (0.3 * p1) + (0.5 * p2) + (0.2 * mepp) + (0.05 * ml)
print("{:.2f}".format(n))