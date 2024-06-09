'''
Faça um programa, usando a estrutura de repetição while, 
para fazer a validação de e-mail usando confirmação. 
Para tanto, seu programa deve ler um e-mail e 
sua respectiva confirmação de senha. 
Caso o e-mail digitado e a confirmação sejam diferentes
o programa deve emitir a mensagem de erro 
"Confirmação falhou!" e novamente solicitar um e-mail e 
sua confirmação até que sejam iguais. 
No caso da confirmação ser bem sucedida 
o programa deve emitir uma mensagem "E-mail confirmado!"

A seguir, um exemplo de teste que será realizado:  
Teste:

meuemail@meuservidor.com

meuEmail@meuservidor.com

Confirmação falhou!

meuemail@meuservidor.com

meuemail@meuservidor.com

E-mail confirmado!
'''

A = True

while A:
  email = input()
  confirmacao = input()

  if email == confirmacao:
    print("E-mail confirmado!")
    A = False
  else:
    print("Confirmação falhou!")
