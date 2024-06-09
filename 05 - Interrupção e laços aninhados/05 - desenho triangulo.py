'''
Escreva um programa que desenhe um triângulo, 
usando um determinado caractere determinado pelo usuária, 
que tenha uma base ímpar b com uma altura igual a h = ceil(b/2). 
A operação ceil{x} retorna o menor número inteiro que 
seja maior ou igual a x. Por exemplo, ceil{3.44} = 4.

Seu programa deve primeiramente testar se b é ímpar. 
Caso não seja, deve retornar a mensagem de erro: 
"A base do triângulo deve ser um número ímpar.". 
Caso o valor de b seja ímpar, o programa deve 
prosseguir com a leitura do caractere a ser usado 
para o desenho e com o desenho do triângulo propriamente dito.

Como exemplo, se b = 7 e o caractere for "*", seu programa deve desenhar o seguinte:

   * 

  ***

 *****

*******

Dica: considerando um retângulo b x h, 
preencha as posições que não pertencem 
ao triângulo com um espaço.
'''

import math

B = int(input())
A = math.ceil(B / 2)

if B % 2 == 0:
    print("A base do triângulo deve ser um número ímpar.")
else:
    char = input()
    stars = char
    space = ""

    for y in range(A):
        for x in range(int((B - ((y * 2) + 1)) / 2)):
            space += " "
        print(space + stars + space)

        space = ""
        stars += char + char