'''
Escreva um programa que leia um inteiro N positivo, 
que irá representar o tamanho de um vetor V. Em seguida, 
leia os valores de cada elemento desse vetor. Ao final, 
verifique se é um vetor onde todos os elementos vêm em duplas.

Uma dupla é formada quando há dois elementos iguais e em posições consecutivas. 
Por exemplo, o vetor [1,1,2,2,3,3] é um vetor de duplas, enquanto [1,1,2,2,2] 
não é um vetor de duplas, pois os quatro primeiros elementos formam duplas, 
mas não restam elementos para o último 2 formar dupla. O vetor [1,2,1,2,3,3] 
também não é um vetor de duplas, pois 1 e 2 não formam uma dupla.

Saídas possíveis (não inclua o til na impressao de "Nao"):

    Eh um vetor de duplas!
    Nao eh um vetor de duplas!


Entradas:

    Tamanho N do vetor (inteiro >1

)
Elementos ai

    que compõem o vetor (inteiros)

Saída:

    Formam duplas ou não


Exemplo 1:
Entradas:

6
1
1
2
2
3
3

Saídas:

Eh um vetor de duplas!


Exemplo 2:
Entradas:

5
1
1
2
2
2

Saídas:

Nao eh um vetor de duplas!


Exemplo 3:
Entradas:

5
1
1
3
3
2

Saídas:

Nao eh um vetor de duplas!


Exemplo 4:
Entradas:

6
1
1
1
1
1
1

Saídas:

Eh um vetor de duplas!
'''

n = int(input())
vec = []
positive = True

for x in range(n):
    vec.append(int(input()))

if n % 2 == 1:
    print("Nao eh um vetor de duplas!")
else:
    for x in range(0, len(vec),2):
        if vec[x] != vec[x+1]:
            print("Nao eh um vetor de duplas!")
            positive = False
            break
    if positive == True:
        print("Eh um vetor de duplas!")