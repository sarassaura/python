'''
Faça um programa que:

    LEIA um valor n e depois leia os n valores de um VETOR de n posições. 
    Em seguida, LEIA também um índice X. Caso o valor de X seja inválido, 
    imprima a mensagem "Valor de X inválido!" e 
    solicite a entrada de X novamente. 
    O programa só deve continuar quando 
    o usuário digitar um valor válido para o índice X.
    Depois, LEIA um índíce Y. Assim como no caso do índice X, 
    se o valor de Y for inválido, imprima a mensagem 
    "Valor de Y inválido!" e solicite a entrada de Y novamente. 
    O programa só deve continuar quando 
    o usuário digitar um valor válido para o índice Y.
    Por fim, o programa deve exibir a SOMA dos valores encontrados 
    nas respectivas POSIÇÕES X e Y e IMPRIMIR 
    "Soma é: v", em que v é o valor da soma dos valores.

Observação: as posições em uma lista em Python iniciam no índice 0. 
Por exemplo, um vetor com 10 posições possui os índices 0 até 9.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Alguns testes que serão realizados:

ENTRADAS 1:

8
3
7
4
3
2
1
7
2
2
6

SAÍDA 1:

Soma é: 11

ENTRADAS 2:

9
1
2
3
4
9
5
1
0
6
9
10
3
1

SAÍDAS 2:

Valor de X inválido!
Valor de X inválido!
Soma é: 6
'''

n = int(input())
vec = [0] * n
invalid = True

for x in range(n):
    vec[x] = int(input())

while invalid:
    X = int(input())

    if X >=0 and X < n:
        invalid = False
    else: 
        print("Valor de X inválido!")

invalid = True

while invalid:
    Y = int(input())

    if Y >=0 and Y < n:
        invalid = False
    else:
        print("Valor de Y inválido!")

print("Soma é: {:d}".format(vec[X] + vec[Y]))