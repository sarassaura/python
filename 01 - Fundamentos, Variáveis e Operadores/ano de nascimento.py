'''
Implemente um algoritmo que leia, via teclado, 
o ano de nascimento de uma pessoa, 
o ano atual e mais um outro ano. 
Depois, calcule e mostre:

a) A idade dessa pessoa;
b) Quantos anos essa pessoa terá em um determinado ano definido, via teclado, pelo usuário.

DICA!!!

A impressão do valor de uma variável no meio de uma frase pode ser realizada da seguinte forma:
print("Em ", ano, ", a idade sera: ", idade, sep="")
OU
print("Em {0}, a idade sera: {1}".format(ano, idade))


Os seguintes testes serão realizados (observe o formato das saídas)

ENTRADAS 1:

1980
2021
2025

SAÍDAS 1:

Idade atual: 41
Em 2025, a idade sera: 45


ENTRADAS 2:

1993
2021
2030

SAÍDAS 2:

Idade atual: 28
Em 2030, a idade sera: 37
'''

print('Digite o ano de nascimento:')
ano_nascimento = int(input())
print('Digite o ano atual:')
ano_atual = int(input())
print('Digite o ano futuro:')
ano_futuro = int(input())

print()

idade = ano_atual - ano_nascimento
idade_futuro = ano_futuro - ano_nascimento

print('Idade atual:',idade)
print("Em {0}, a idade sera: {1}".format(ano_futuro, idade_futuro))