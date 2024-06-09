'''
Escreva um programa que, lidos dois vetores ordenados e 
sem valores repetidos v1 e v2, de tamanhos n1 e n2, 
respectivamente, retorne um vetor ordenado de tamanho n3, 
contendo todos os elementos não repetidos de v1 e v2. 
Internamente, v1 e v2 não possuem valores repetidos, 
mas podem ter valores que aparecem tanto em v1 como em v2!

O programa deve primeiramente ler n1 e o conteúdo de v1. 
Depois, ler n2 e os valores em v2.

Por exemplo, se n1= 4 com v1=[1, 2, 5, 8] e 
n2 = 3 com v2 = [0, 2, 9], 
o vetor a ser mostrado com os elementos separados por espaços, 
que representa a união dos dois vetores será [0, 1, 2, 5, 8, 9]. 

Dica: você pode percorrer os índices dos dois vetores com um laço while, 
testando as condições em que os valores são maiores, 
menores ou iguais para ordenamento dos vetores. 
Observe que quando o teste dos dois vetores 
retornar valores iguais isso indicará valores repetidos!

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

n1 = int(input())

v1 = [0] * n1

for x in range(n1):
    v1[x] = int(input())

n2 = int(input())

v2 = [0] * n2

for x in range(n2):
    v2[x] = int(input())

v3 = []

i = 0
j = 0
c = 0

while c < (n1 + n2):
    if i > n1 - 1:
        v3.append(v2[j])
        j += 1
    elif j > n2 - 1:
        v3.append(v1[i])
        i += 1
    else:
        if v1[i] < v2[j]:
            v3.append(v1[i])
            i += 1
        elif v2[j] < v1[i]:
            v3.append(v2[j])
            j += 1
        else:
            v3.append(v1[i])
            i += 1
            j += 1
            c += 1
    c += 1

for x in range(len(v3)):
    print(v3[x], sep=' ', end=' ')