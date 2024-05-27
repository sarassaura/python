'''
Faça um programa que integre e derive polinômios. 
Cada polinômio é definido por um vetor que 
contém seus coeficientes, ordenado do maior para o menor grau.

Por exemplo, o polinômio de grau dois 3x^2+2x+12 terá um vetor de coeficientes 
v=[3,2,12]. Sua integral será I=[1,1,12,0], ]
equivalente ao polinômio x^3 + x^2 + 12x, e sua derivada será D=[6,2], 
equivalendo ao polinômio 6x+2. O programa deve, primeiramente, 
receber o valor do maior grau g do polinômio. Em seguida, 
deve ler (g+1) coeficientes. Depois, calcular e mostrar 
(a) o vetor de coeficientes da integral do polinômio; e 
(b) o vetor de coeficientes da derivada do polinômio.

Note que os coeficientes dos vetores da integral e 
da derivada são números reais e 
devem ser mostrados com duas casas decimais.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Exemplo de Entradas:
2
3
2
12
Saídas:
1.00 1.00 12.00 0.00
6.00 2.00
'''

g = 0
v = []
i = []
d = []

g = int(input())

for x in range(g+1):
    v.append(int(input()))

for y in range(g+1):
    i.append(v[y] / ((g-y) + 1))

i.append(0)

for y in range(g):
    d.append(v[y] * (g-y))

for z in range(g+2):
    print("{:.2f}".format(i[z]), sep=' ', end=' ')

print()

for z in range(g):
    print("{:.2f}".format(d[z]), sep=' ', end=' ')