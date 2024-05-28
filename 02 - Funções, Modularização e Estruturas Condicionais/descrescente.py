'''
Ler dois números do tipo float e apresentá-los em ordem decrescente. 
Supor que não sejam iguais.

Os seguintes testes serão realizados,   

ENTRADA 1:

3.0
2.0

SAÍDA 1:

3.0
2.0


ENTRADA 2:

1.4
10.5

SAÍDA 2:

10.5
1.4
'''

X = float(input())
Y = float(input())

if X > Y:
  print(X)
  print(Y)
else:
  print(Y)
  print(X)