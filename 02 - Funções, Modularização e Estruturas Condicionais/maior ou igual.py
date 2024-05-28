'''
Implementar um algoritmo que faça a leitura de um determinado valor e 
verifique se o valor é maior ou igual a três. 
Se sim, deve-se imprimir "É maior ou igual!"". 
Caso contrário, deve ser impresso "É menor!".

Alguns testes que serão realizados:

ENTRADA 1:

3

SAÍDA 1:

É maior ou igual!


ENTRADA 2:

1

SAÍDA 2:

É menor!


ENTRADA 3:

87

SAÍDA 3:

É maior ou igual!
'''

X = float(input())

if X >= 3:
  print('É maior ou igual!')
else:
  print('É menor!')