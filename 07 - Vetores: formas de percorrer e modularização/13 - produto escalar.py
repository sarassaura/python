'''
Faça um programa que leia dois conjuntos de números reais, 
armazenando-os nos vetores x e y e 
calcule o produto escalar entre eles. 

Os conjuntos têm n = 5 elementos cada um e 
devem ser lidos da seguinte forma: 
primeiro leia todos os elemento do vetor x e 
depois leia todos os elementos do vetor y.

Imprimir os dois conjuntos e o produto escalar, dado por:

x * y = ∑(n−1,i=0) (x[i] * y[i])


A saída do programa será: 
"O produto escalar vale Pe.", 
em que Pe deve ser mostrado com duas casas decimais.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

v1 = [0] * 5
v2 = [0] * 5
escalar = 0

for x in range(5):
    v1[x] = float(input())

for y in range(5):
    v2[y] = float(input())

for z in range(5):
    escalar += v1[z] * v2[z]

print("O produto escalar vale {:.2f}.".format(escalar))