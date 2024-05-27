'''
Escreva um programa que desenhe um retângulo composto 
de x (x > 2) linhas e y colunas (y > 2), no qual 
o perímetro é composto por um símbolo "+". 

Como exemplo, se x = 3 e y = 7, 
seu programa deve desenhar o seguinte:

+++++++
+     +
+++++++

Caso x ou y esteja fora dos padrões o programa deve 
emitir uma mensagem de erro: 
"Dimensões fora das especificações.".
'''

X = int(input())
Y = int(input())
border = "++"
middle = "+"

if X <= 2 or Y <= 2:
    print("Dimensões fora das especificações.")
else:
    for space in range(Y - 2):
        border += "+"
        middle += " "

    middle += "+"

    print(border)

    for line in range(X - 2):
        print(middle)

    print(border)