'''
Faça um programa que fique lendo números do usuário até que ele digite 0. 
Quando isso ocorrer, mostre o valor da média aritmética de todos os 
números lidos (imprima o valor com duas casas decimais após a vírgula).

Entrada:

    Uma sequência de números inteiros. A leitura é encerrada quando o usuário digitar 0 (zero).

Saída:

    Média de todos os valores lidos.
'''

sum = 0
n = 0

while True:
    num = int(input())
    sum += num
    if num == 0:
        if n == 0:
            n = 1
        print("{:.2f}".format(sum / n))
        break
    n += 1