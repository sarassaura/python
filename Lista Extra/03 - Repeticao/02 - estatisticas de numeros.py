'''
Escreva um programa que leia um inteiro n e então leia n números inteiros. 
Ao final, o programa deve imprimir os seguintes valores 
sobre a sequência de n valores lidos:

    Soma (dos n números)
    Média
    Mínimo
    Máximo


Entrada:

    Um número inteiro n
    n números inteiros

Saída:

    Soma
    Média (imprima com duas casas decimais após a vírgula)
    Mínimo
    Máximo
'''

n = int(input())
minimo = float("inf")
maximo = float("-inf")
sum = 0

for x in range(n):
    y = float(input())
    sum += y
    if y > maximo:
        maximo = y
    if y < minimo:
        minimo = y

print(int(sum))
print("{:.2f}".format(sum / n))
print(int(minimo))
print(int(maximo))