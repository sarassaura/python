'''
Faça um programa que preencha um vetor com 5 números reais. 
Em seguida, calcule e mostre na tela a QUANTIDADE de 
números negativos e a SOMA dos números positivos desse vetor. 
Além disso, deve-se verificar se um determinado número, 
definido pelo usuário (por meio de um input),
EXISTE na lista, imprimindo "Existe!" ou "Não existe!".

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Para este exercício, os seguintes testes serão executados:

ENTRADAS 1:

1
2
7
8
5
9


SAÍDAS 1:

0
23
Não existe!

ENTRADAS 2:

-5
-4
3
-2
1
3


SAÍDAS 2:

3
4
Existe!

ENTRADAS 3:

-1
-4
-3
-9
-5
9

SAÍDAS 3:

5
0
Não existe!
'''

vec = [0] * 5
negativos = 0
soma_positivos = 0
existe = False

for x in range(5):
    vec[x] = float(input())
    
    if vec[x] < 0:
        negativos += 1
    else:
        soma_positivos += vec[x]

number = float(input())

for x in range(5):
    if number == vec[x]:
        existe = True

print(negativos)
print(int(soma_positivos))

if existe:
    print("Existe!")
else:
    print("Não existe!")