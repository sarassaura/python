'''
Faça um programa, usando a estrutura de repetição while, 
que leia um número inteiro positivo N e 
imprima quantos algarismos este número possui.

Para resolver este problema você pode tomar o número e dividí-lo por 10. 
Então, sucessivamente dividir a parte do resultado por 10, 
até que o resultado seja 0. 

Por exemplo, se o número for 26578:

Passo 1: 26578 / 10 =  2657,8 (A parte inteira é 2657)

Passo 2: 2657/10 = 265,7 (A parte inteira é 265)

Passo 3: 265/10 = 26,5 (A parte inteira é 26)

Passo 4: 26/10 = 2,6 (A parte inteira é 2)

Passo 5: 2/10 = 0,2 (A parte inteira é 0) --> Condição de parada da estrutura de repetição.

Nesse algoritmo, o número de passos utilizados define o número de algarismos. 
Logo, o número de algarismos é igual a 5.

Para obter a parte inteira de uma divisão você pode usar o operado "//" 
ou converter o resultado para uma variável inteira usando "int()".

A saída do programa deverá ter a forma: "O número 26578 possui 5 algarismos."

A seguir, um dos testes que será realizado:  
ENTRADA 01:

644890

SAIDAS 01:

O número 644890 possui 6 algarismos.
'''

N = int(input())

result = "O número {:d} possui".format(N)

steps = 0

while N > 0:
  steps += 1
  N = N // 10

result += " {:d} algarismos.".format(steps)

print(result)