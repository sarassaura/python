'''
Faça um programa que calcule o conceito final de 
um aluno em uma disciplina. O programa irá receber, 
respectivamente, as notas de três testes, um a um, 
e a nota de duas provas, uma a uma.

A seguir, defina e imprima a Nota Final (NF) 
formatada com duas casas decimais e o 
Conceito Final do aluno de acordo com a definição a seguir:

NF = 0.2*T + 0.4*P1 + 0.4*P2


T é a média aritmética dos três testes;
P1 é a nota da primeira prova;
P2 é a nota da segunda prova.

Cálculo do Conceito Final (CF):
9.0 ≤ NF ≤ 10.0 ⟹ CF = A
7.5 ≤ NF < 9.0 ⟹ CF = B
6.0 ≤ NF < 7.5 ⟹ CF = C
5.0 ≤ NF < 6.0 ⟹ CF = D
NF < 5.0 ⟹ CF = F

Entradas:

    Nota obtida no Teste1 (número real);
    Nota obtida no Teste2 (número real);
    Nota obtida no Teste3 (número real);
    Nota obtida na primeira prova (número real);
    Nota obtida na segunda prova (número real).

Saídas:

    Nota Final formatada com duas casas decimais;
    Conceito Final.



Exemplo:
Entradas:

1
2
4
5
7

Saídas:

5.27
D

Exercício elaborado por Gabriel Ângelo Sembenelli (2022).
'''

t1 = float(input())
t2 = float(input())
t3 = float(input())
p1 = float(input())
p2 = float(input())

final = (0.2 * (t1 + t2 + t3) / 3) + (0.4 * p1) + (0.4 * p2)

print("{:.2f}".format(final))

if final >= 9 and final <= 10:
    print("A")
elif final >= 7.5 and final < 9:
    print("B")
elif final >= 6 and final < 7.5:
    print("C")
elif final >= 5 and final < 6:
    print("D")
else:
    print("F")