'''
Implemente um algoritmo que leia três números (a, b e c) e então calcule:

1) O quadrado de a;
2) O cubo de a;
3) Resto da divisão de b por c.

Dica!!!

O resto da divisão deve ser calculado usando o operador % (módulo). 
Para isso, basta:
a = 10
b = 3
resto = a % b


Os seguintes testes serão realizados (observe o formato das saídas).


ENTRADAS 1:

2
3
4

SAÍDAS 1:

Quadrado de 2: 4
Cubo de 2: 8
Resto de 3 por 4: 3


ENTRADAS 2:

5
20
4

SAÍDAS 2:

Quadrado de 5: 25
Cubo de 5: 125
Resto de 20 por 4: 0
'''

a = int(input())
b = int(input())
c = int(input())

resto = b % c

print('Quadrado de {0}: {1}'.format(a, pow(a,2)))
print('Cubo de {0}: {1}'.format(a, pow(a,3)))
print('Resto de {0} por {1}: {2}'.format(b,c,resto))