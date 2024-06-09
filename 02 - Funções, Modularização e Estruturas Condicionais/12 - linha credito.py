'''
A prefeitura de uma cidade abriu uma linha de crédito para os funcionários estatutários. 
O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. 
Implemente um algoritmo que leia o salário bruto e o valor da prestação e 
informe se o empréstimo pode ("Empréstimo Liberado!") ou 
não ("Empréstimo Negado!") ser concedido.

Os seguintes testes serão realizados,   

ENTRADAS 1:

1000
400

SAÍDA 1:

Empréstimo Negado!


ENTRADAS 2:

3000
500

SAÍDA 2:

Empréstimo Liberado!


ENTRADAS 3:

6000
1800

SAÍDA 2:

Empréstimo Liberado!
'''

salario_bruto = float(input())
prestação = float(input())

valor_maximo = salario_bruto * 0.3

if prestação <= valor_maximo:
  print('Empréstimo Liberado!')
else:
  print('Empréstimo Negado!')