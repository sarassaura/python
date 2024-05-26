'''
Um feirante vende maçãs a R$ 1,50 cada. 
Há um desconto de 20% no valor da compra se 
pelo menos uma dúzia de maçãs forem compradas. 
Escreva um programa que leia o número de maçãs compradas, 
calcule e escreva o custo total da compra.

A saída do programa deve ser: "O custo de N maçãs é R$ C.", 
sendo N o número inteiro de maçãs compradas e 
o C o custo em reais, mostrado com duas casas decimais.
'''

maca = 1.5

quantidade = int(input())

if quantidade >= 12:
    custo = quantidade * 1.5 * 0.8
    print("O custo de {:d} maçãs é R$ {:.2f}.".format(quantidade, custo))
else:
    custo = quantidade * 1.5
    print("O custo de {:d} maçãs é R$ {:.2f}.".format(quantidade, custo))