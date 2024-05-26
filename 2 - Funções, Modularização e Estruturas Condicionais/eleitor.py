'''
Escreva um programa que leia o ano atual e 
o ano de nascimento de uma pessoa, 
escrevendo uma mensagem que diga se ela poderá ou não votar este ano. 
Não é necessário considerar o mês em que a pessoa nasceu.

A mensagem caso a pessoa possa votar é: "Habilitado a votar!". 
Caso contrário: "Não habilitado a votar!".
'''

ano_atual = int(input())
ano_nascimento = int(input())

if (ano_atual - ano_nascimento) >= 16:
  print('Habilitado a votar!')
else:
  print('Não habilitado a votar!')