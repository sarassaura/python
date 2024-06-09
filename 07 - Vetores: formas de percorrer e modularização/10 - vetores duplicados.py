'''
Escreva um programa que leia um valor inteiro n1, 
depois leia os n1 valores de um vetor1. 
Após isso, leia um valor inteiro n2 e os n2 valores de um vetor2. 
Todos os elementos dos vetores são números inteiros.

Observe que os valores de entrada são 
apresentados cada um em uma linha. 
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

Após a leitura dos vetores, 
o programa deve imprimir os valores dos dois vetores 
(cada vetor em uma linha, separe cada elemento por um caractere espaço) e,
ao final, imprima "Vetor duplicado" se os valores no vetor1 são o dobro 
dos valores nas posições correspondentes no vetor2 ou "Erro" caso contrário. 

Neste exercício, considere que um vetor é duplicado se 
tem o mesmo TAMANHO do outro vetor e se os valores em 
cada índice do vetor1 são iguais ao dobro dos valores nas 
posições correspondentes no vetor2. 
Por exemplo: para os vetores [22, 66, 44] e [11, 33, 22], 
deve-se imprimir "Vetor duplicado".

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

valid = True

n1 = int(input())
v1 = [0] * n1

for x in range(n1):
    v1[x] = int(input())

n2 = int(input())
v2 = [0] * n2

for y in range(n2):
    v2[y] = int(input())

for x in range(n1):
    print(v1[x], end=' ')

print()

for y in range(n2):
    print(v2[y], end=' ')

print()

r = v1[0] / v2[0]

if n1 == n2:
    for z in range(n1):
        if v1[z] / v2[z] != r:
            valid = False
            break
else: 
    valid = False

if valid:
    print("Vetor duplicado")
else:
    print("Erro")