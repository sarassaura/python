'''
Escreva um programa que leia um valor inteiro n1, 
depois leia os n1 valores de um vetor1. 
Após isso, leia um valor inteiro n2 e os n2 valores de um vetor2. 
Todos os elementos dos vetores são números inteiros.

Observe que os valores de entrada são apresentados cada um em uma linha. 
Por exemplo:

n1=3
11
33
22
n2=4
55
44
77
66

Após a leitura dos vetores, o programa deve imprimir 
os valores dos dois vetores 
(cada vetor em uma linha e os elementos devem 
ser separados pelo caractere espaço) e, ao final, 
deve-se imprimir "OK", se o vetor2 tem os mesmos valores do vetor1, 
mesmo que em ordem diferente, ou "Erro" caso contrário. 
Assume que não há valores repetidos inseridos em cada vetor.

Entradas 1: vetor1=[11, 33, 22]; vetor2=[11, 33, 22]
Saídas 1:
11 33 22
11 33 22
OK

Entradas 2: vetor1=[11, 22, 33]; vetor2=[33, 11, 22]
Saídas 2:
11 22 33
33 11 22
OK

Entradas 3: vetor1=[11, 22, 33]; vetor2=[11, 33, 55]
Saídas 3: 
11 22 33
11 33 55
Erro

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

n1 = int(input())
v1 = [0] * n1
repeated = {}
valid = True

for x in range(n1):
    v1[x] = int(input())
    try:
        repeated[v1[x]] += 1
    except:
        repeated[v1[x]] = 1

n2 = int(input())
v2 = [0] * n2

for y in range(n2):
    v2[y] = int(input())
    try:
        repeated[v2[y]] += 1
    except:
        repeated[v2[y]] = 1

for x in range(n1):
    print(v1[x], end=' ')

print()

for y in range(n2):
    print(v2[y], end=' ')

print()

for x in range(n1):
    if repeated[v1[x]] != 2:
        valid = False

for y in range(n2):
    if repeated[v2[y]] != 2:
        valid = False

if valid:
    print("OK")
else:
    print("Erro")