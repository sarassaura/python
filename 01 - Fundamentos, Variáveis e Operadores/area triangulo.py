'''
Implemente um algoritmo que calcule a área de um triângulo 
(area = (base*altura) / 2), 
sendo que a base e a altura devem ser definidas pelo usuário (teclado).

Observação: imprima o valor da área usando uma casa decimal. 
Para formatar a saída em Python, pode-se utilizar o seguinte código:

numero = 5.07507
print("Valor = {:.1f}".format(numero))

Os seguintes testes serão realizados.

ENTRADAS 1:

2
3

SAÍDA 1:

3.0


ENTRADAS 2:

1
3

SAÍDA 2:

1.5
'''

print('Digite a base do triangulo:')
base = float(input())
print('Digite a altura do triangulo:')
altura = float(input())

print()

area = (base * altura) / 2

print("{:.1f}".format(area))