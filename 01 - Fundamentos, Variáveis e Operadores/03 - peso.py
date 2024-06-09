'''
Implemente um algoritmo que calcule e mostre o peso, informado pelo usuário, 
se a pessoa engordar e emagrecer 34% e 13% sobre o peso digitado, respectivamente.

Observação: imprima os valores usando apenas uma casa decimal. 
Para formatar a saída em Python é possível utilizar o seguinte código:

numero = 5.07
print("Valor = {:.1f}".format(numero))

Os seguintes testes serão realizados (observe o formato das saídas):

ENTRADA 1:

40

SAÍDAS 1:

Peso (engordou): 53.6
Peso (emagreceu): 34.8


ENTRADA 2:

78

SAÍDAS 2:

Peso (engordou): 104.5
Peso (emagreceu): 67.9
'''

print('Digite seu peso:')
peso = int(input())

print()

plus = (peso * 1.34)
minus = (peso * 0.87)

print("Peso (engordou): {:.1f}".format(plus))
print("Peso (emagreceu): {:.1f}".format(minus))