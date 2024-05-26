'''
Implemente um algoritmo que leia o sexo (0 para homem e 1 para mulher) 
e a altura de uma pessoa, calcule e mostre seu peso ideal. Sabendo que:

    Para homens: (72,7 * h) – 58
    Para mulheres (62,1 * h) – 44,7

Ps: O resultado (saída) deve ser impresso com DUAS casas decimais.

Os seguintes testes serão realizados,   

ENTRADAS 1:

0
1.77

SAÍDA 1:

Peso ideal é: 70.68


ENTRADAS 2:

1
1.65

SAÍDA 2:

Peso ideal é: 57.77
'''

sexo = int(input())
altura = float(input())

if sexo == 0:
  print('Peso ideal é: {:.2f}'.format((72.7 * altura) - 58))
elif sexo == 1:
  print('Peso ideal é: {:.2f}'.format((62.1 * altura) - 44.7))