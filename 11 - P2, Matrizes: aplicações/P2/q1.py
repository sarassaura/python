'''
Faça um programa que leia um valor inteiro N e 
os elementos de um vetor V de números reais com N elementos. 
Após isso, deve-se criar um outro vetor W com 
tamanho N/2 para armazenar a soma dos elementos do 
vetor V da seguinte forma:

    O primeiro elemento do vetor W deve armazenar a 
    soma dos valores do primeiro e último elemento de V;
    O segundo elemento do vetor W deve armazenar a 
    soma dos valores do segundo e do penúltimo elemento do vetor V;
    O terceiro elemento do vetor W deve armazenar a 
    soma dos valores do terceiro e antepenúltimo elemento do 
    vetor V e assim por diante.

Por fim, o algoritmo deve imprimir, na mesma linha, 
os elementos do vetor W criado.

Por exemplo, se V = [1.1, 2.4, 3.5, 4.6, 4.5], o vetor W = [5.6, 7.0]. 
Observa-se que, se o tamanho do vetor V for ímpar, 
o elemento central (3.5) do vetor V não terá um par para 
ser somado e, portanto, NÃO fará parte do vetor W.

IMPORTANTE: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, sort, reverse, index, count, etc.

Alguns testes que serão realizados:

ENTRADAS 1

5
1.1
2.4
3.5
4.6
4.5

SAÍDAS 1

5.6 7.0

ENTRADAS 2

10
11
20
30
80
90
30
50
60
70
10

SAÍDAS 2

21.0 90.0 90.0 130.0 120.0

ENTRADAS 3

7
15.5
25.5
35.5
999
11.1
15.1
10.1

SAÍDAS 3

25.6 40.6 46.6

ENTRADAS 4

2
1.5
0.8

SAÍDAS 4

2.3

ENTRADAS 5

4
9.5
50
20
2.7

SAÍDAS 5

12.2 70.0
'''

n = int(input())
v = [0] * n
half = n // 2
w = [0] * half

for y in range(n):
  v[y] = float(input())

for x in range(half):
  w[x] = v[x] + v[n - 1 - x]

print(*w)