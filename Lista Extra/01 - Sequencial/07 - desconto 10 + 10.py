'''
Uma loja aplica descontos anunciando da seguinte forma: 
10% + 10%. Ou seja, primeiro reduz o valor total em 10% e 
depois reduz mais 10% sobre o total já descontado. 
Escreva um programa que receba o valor de um produto e 
imprima o valor após o desconto 10% + 10%.

Por exemplo, para o valor 50, após o desconto, o valor será 40,50

Entrada:

    Valor total

Saída:

    Valor com o desconto (utilize duas casas decimais)

'''

valor = float(input())

print(valor * 0.9 * 0.9)