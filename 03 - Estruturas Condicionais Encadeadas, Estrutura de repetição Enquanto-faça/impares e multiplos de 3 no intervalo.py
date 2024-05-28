'''
Escreva um programa, usando a estrutura de repetição while, 
para ler as extremidades de um intervalo fechado [a, b] e 
contar a quantidade de números ímpares que 
também sejam múltiplos de 3 nesse intervalo.

A saída do programa deve ser: 
"Tem c número(s) ímpar(es) múltiplo(s) de 3 entre a e b.", 
em que c é o número obtido pelo programa, e 
a e b são as extremidades do intervalo.
'''

A = int(input())
B = int(input())
count = A
c = 0

while count < B + 1:
  if (count % 2 == 1) and (count % 3 == 0):
    c += 1
  count += 1

print("Tem {:d} número(s) ímpar(es) múltiplo(s) de 3 entre {:d} e {:d}.".format(c,A,B))