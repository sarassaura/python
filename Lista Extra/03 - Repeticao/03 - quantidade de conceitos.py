'''
Faça um programa que receba um valor n, leia n notas de alunos e mostre 
quantos alunos tiveram cada conceito e a média de todos 
com duas casas decimais.

Neste exercício, considere a seguinte a regra para 
conversão de nota para conceito:

>=9 e <=10 : A
>=8 e <9: B
>=7 e <8: C
>=5 e <7: D
<5: F

Exemplo:
Entradas:

7
0
2
4
9
10
7
8
Saídas (observação: "Media" deve ser impresso sem acento):

A: 2
B: 1
C: 1
D: 0
F: 3
Media: 5.71

Exercício elaborado por Marcos Gasques (2022).
'''

n = int(input())
sum = 0

A = 0
B = 0
C = 0
D = 0
F = 0

for x in range(n):
    nota = int(input())
    sum += nota
    if nota >= 9 and nota <= 10:
        A += 1
    elif nota >= 8:
        B += 1
    elif nota >= 7:
        C += 1
    elif nota >= 5:
        D += 1
    else:
        F += 1 

print("A: {:d}".format(A))
print("B: {:d}".format(B))
print("C: {:d}".format(C))
print("D: {:d}".format(D))
print("F: {:d}".format(F))
print("Media: {:.2f}".format(sum / n))