'''
Escreva um programa que leia o endereço de e-mail do remetente, 
o endereço de e-mail do destinatário e o texto da mensagem. 
Após isso, imprima o e-mail no seguinte formato:

De:<endereço remetente>
Para:<endereço destinatário>
Mensagem:<texto da mensagem>

Exemplo:

De:funcionario@empresa.com
Para:gerente@empresa.com
Mensagem:Segue relatorio de vendas desta semana.

Entrada:

    endereço de e-mail do remetente
    endereço de e-mail do destinatário
    texto da mensagem

Saída:

    e-mail formatado conforme enunciado
'''

print('Escreva o email do remetente:')
x = input()
print('Escreva o email do destinatário:')
y = input()
print('Escreva a mensagem:')
z = input()

print()

print('De: ',x, sep='')
print('Para: ',y, sep='')
print('Mensagem: ',z, sep='')