'''
Faça um programa, usando a estrutura de repetição while, 
que leia um número inteiro N e depois imprima 
os N primeiros números naturais ÍMPARES em uma linha e 
os N primeiros PARES em outra linha. 
Inclua um caractere espaço entre cada número impresso.

Os seguintes testes serão realizados,  

ENTRADA 01:

10

SAIDAS 01:

1 3 5 7 9 11 13 15 17 19
0 2 4 6 8 10 12 14 16 18


ENTRADA 02:

5

SAIDAS 02:

1 3 5 7 9
0 2 4 6 8
'''

N = int(input())
count = 0
impares = "1"
pares = "0"

while count < N - 1:
  count += 1
  pares += " " + str(count * 2)

count = 0

while count < N - 1:
  count += 1
  impares += " " + str(count * 2 + 1)

  
print(impares)
print(pares)