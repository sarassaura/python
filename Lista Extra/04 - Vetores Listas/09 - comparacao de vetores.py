'''
Escreva um programa que leia dois vetores (A e B) de mesmo comprimento n. 
Para isso, o programa deve ler um valor inteiro n (comprimento), 
ler o n valores de um dos vetores e depois os n valores do outro vetor. 
Ao final, o programa deve imprimir "SIM" se um vetor for o resultado de 
uma multiplicação de todos os elementos do outro pelo mesmo valor, 
ou "NAO" caso contrário.

Por exemplo, considere os vetores A = [1, 2, 5, 10] e B = [3, 6, 15, 30]. 
Neste caso, o programa deve imprimir "SIM", pois o vetor B é resultado 
da multiplicação de todos os elementos de A por 3.

Outro exemplo: considere os vetores A = [1, 2, 5, 10] e B = [3, 6, 15, 90]. 
Neste caso, o programa deve imprimir "NAO", pois o vetor B não é resultado 
da multiplicação de todos os elementos de A por um mesmo valor. 
Os três primeiros números foram multiplicados por 3, mas o quarto foi multiplicado por 9.

Observação: após a leitura do valor n, 
os elementos de cada vetor estão todos 
dispostos em apenas uma linha. Por exemplo:

4
1 2 5 10
3 6 15 30

Para ler elementos em uma mesma linha em Python ou em Java, 
pode ser usada uma estratégia similar àquela apresentada 
no enunciado do 08 - Vetor crescente.

Entrada

    Comprimento (n)
    n elementos do primeiro vetor
    n elementos do segundo vetor

Saída

    SIM/NAO (dependendo se um vetor for o resultado de uma 
    múltiplicação de todos os elementos do outro por um mesmo valor)
'''

n = int(input())
yes = True

v1 = [0] * n

itens_linha = input().split(" ")
for i in range(n):
    v1[i] = int(itens_linha[i])

v2 = [0] * n

itens_linha = input().split(" ")
for i in range(n):
    v2[i] = int(itens_linha[i])

r = v1[0] / v2[0]

for x in range(1, n):
    if v1[x] / v2[x] != r:
        print("NAO")
        yes = False
        break

if yes == True:
    print("SIM")