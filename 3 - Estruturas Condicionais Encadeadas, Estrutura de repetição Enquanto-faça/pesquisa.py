'''
Realizou-se uma pesquisa com 3 pessoas que responderam à seguinte pergunta:

Quantos filhos você tem?

Escreva um algoritmo para processar essa pesquisa informando 
quantas pessoas possuem até 2 filhos e quantas possuem mais de 2 filhos.

Os seguintes testes serão realizados,  
ENTRADAS 01:

1
2
1

SAIDAS 01:

Ate dois filhos: 3
Mais de dois filhos: 0

ENTRADAS 02:

3
4
5

SAIDAS 02:

Ate dois filhos: 0
Mais de dois filhos: 3

ENTRADAS 03:

1
4
2

SAIDAS 03:

Ate dois filhos: 2
Mais de dois filhos: 1

ENTRADAS 04:

1
5
3

SAIDAS 04:

Ate dois filhos: 1
Mais de dois filhos: 2
'''

A = int(input())
B = int(input())
C = int(input())

ate_dois = 0
mais_dois = 0

for x in (A,B,C):
    if x > 2:
        mais_dois += 1
    else:
        ate_dois += 1

print("Ate dois filhos:", ate_dois)
print("Mais de dois filhos:", mais_dois)