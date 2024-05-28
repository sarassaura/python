'''
Uma empresa de logística gostaria de saber a distância 
a ser percorrida em diversas entregas.

Escreva um programa que leia os valores de x e de y 
(coordenadas da empresa de logística). Após isso, 
leia um valor inteiro n e os n valores de um vetor. 
Todos os elementos do vetor são números inteiros. 
Esse vetor armazena as coordenadas das diversas entregas e 
tem o seguinte formato: 
[x1, y1, x2, y2, x3, y3, ... , x(n/2), y(n/2)]. Ou seja, 
a cada duas posições no vetor, há uma coordenada (x, y).

Após a leitura dos valores, 
o programa deve imprimir os valores do vetor 
(separando cada elemento por um caractere espaço) e, ao final, 
deve-se imprimir a distância da empresa até cada entrega. 
Vale ressaltar que as distâncias devem ser impressas na mesma linha 
(separadas por um caractere espaço) e com duas casas decimais.

Cálculo da distância: neste exercício, 
considere o seguinte cálculo para obter a distância:

d=((x2−x1)^2 + (y2−y1)^2)^(0.5)

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

a = []
d = []
x = 0
y = 0

x = int(input())
y = int(input())
n = int(input())

for z in range(n):
    a.append(int(input()))

for z in range(n):
    print(a[z], sep=' ', end=' ')

print()

for z in range(0,n,2):
    d.append(((a[z] - x)**2 + (a[z+1] - y)**2)**0.5)

for z in range(n//2):
    print("{:.2f}".format(d[z]), sep=' ', end=' ')