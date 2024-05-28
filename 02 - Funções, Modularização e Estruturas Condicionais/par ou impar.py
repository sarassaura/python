'''
Ler um número inteiro e apresentar uma mensagem 
informando se o número é par ou ímpar. 

Os seguintes testes serão realizados,

ENTRADA 1:

2

SAÍDA 1:

É par!


ENTRADA 2:

3

SAÍDA 2:

É ímpar!


ENTRADA 3:

22

SAÍDA 2:

É par!
'''

X = int(input())

if (X % 2) == 0:
  print('É par!')
else:
  print('É ímpar!')