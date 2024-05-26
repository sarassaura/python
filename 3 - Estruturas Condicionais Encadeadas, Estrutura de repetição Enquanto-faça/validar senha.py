'''
Faça um algoritmo que verifique a validade de uma senha fornecida pelo usuário. 
Sabendo que a senha é UFABC ou ufabc, imprimir mensagem de 
"Acesso Liberado!" ou "Acesso Negado!".

Os seguintes testes serão realizados,   

ENTRADA 1:

UFABC

SAÍDA 1:

Acesso Liberado!


ENTRADA 2:

ufabc

SAÍDA 2:

Acesso Liberado!


ENTRADA 3:

teste

SAÍDA 2:

Acesso Negado!
'''

senha = input()

if senha == "UFABC" or senha == "ufabc":
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")