'''
Faça um programa que leia uma string e 
determine se ela termina com a letra s, 
seja minúscula ou maiúscula.

Seu programa deve emitir uma mensagem 
"Termina com s!" se a string terminar 
com a letra s ou "Não termina com s!" 
se a string não terminar com essa letra.  

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, sort, in, reverse, index, count, etc.

Alguns testes que serão executados:

ENTRADA 01:

Animais

SAÍDA 01:

Termina com s!

ENTRADA 02:

Início

SAÍDA 02:

Não termina com s!
'''

s = input()

char = s[len(s) - 1]

if char == "S" or char == "s":
    print("Termina com s!")
else:
    print("Não termina com s!")