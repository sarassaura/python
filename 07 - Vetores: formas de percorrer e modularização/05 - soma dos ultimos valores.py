'''
Faça um programa que, continuamente, 
leia e armazene valores inteiros em 
um vetor até que o valor -1 seja lido. 
Neste caso o valor -1 não deve ser acrescentado ao vetor.

Após a leitura dos dados seu programa deve 
mostrar a soma dos dois últimos valores no vetor.

Dica: para este programa você pode usar 
o operador len(), que retorna o tamanho de um vetor.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.

Para este exercício, os seguintes testes serão executados:

ENTRADAS 1:

1
2
10
8
5
-1


SAÍDA 1:

13

ENTRADAS 2:

-5
-4
3
-2
1
3
0
-1


SAÍDA 2:

3

ENTRADAS 3:

0
-4
-3
9
-5
-1

SAÍDA 3:

4
'''

vec = []

while True:
    temp = int(input())

    if temp != -1:
        vec.append(temp)
    else:
        break

print(vec[len(vec) - 1] + vec[len(vec) - 2])