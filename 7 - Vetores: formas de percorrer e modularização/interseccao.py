'''
Faça um programa que leia dois vetores x e y de 
5 elementos inteiros cada um e crie um vetor I 
que seja a intersecção entre os 2 vetores x e y. 
Ou seja, que contém apenas os números que 
estão presentes em ambos os vetores. 
Os vetores devem ser lidos sequencialmente, isto é, 
primeiro lê-se o vetor x e depois o vetor y. 
O vetor intersecção não deve conter números repetidos. 
Não use o operador "&" do Python.

A saída do programa deverá ser: 
"O vetor intersecção é I", em que I é o vetor intersecção.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

v1 = [0] * 5
v2 = [0] * 5
repeated = {}

for x in range(5):
    v1[x] = int(input())
    try:
        repeated[v1[x]] += 1
    except:
        repeated[v1[x]] = 1

for y in range(5):
    v2[y] = int(input())
    try:
        repeated[v2[y]] += 1
    except:
        repeated[v2[y]] = 1

i = []

for z in range(5):
    if repeated[v1[z]] == 2:
        i.append(v1[z])
        repeated[v1[z]] = 0

for z in range(5):
    if repeated[v2[z]] == 2:
        i.append(v2[z])
        repeated[v2[z]] = 0

print("O vetor intersecção é", end=' ')
print(i)