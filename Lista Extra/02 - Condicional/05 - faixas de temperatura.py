'''
Foi encontrado um dispositivo que possui um sistema 
que mostra as seguintes  mensagens, dependendo da 
temperatura medida: Muito Baixa, Baixa, Normal, Alta 
e Muito Alta. O dispositivo usa as faixas exibidas 
na figura a seguir:

https://drive.google.com/file/d/18AkCBGGXHceJBUi4iu-C1lguUb9Z2rIW/view?usp=drive_link

Escreva um programa que leia o valor da temperatura e mostre qual a mensagem que seria exibida. 

Entrada:

Valor da temperatura.
Saída:

Mensagem (de acordo com a temperatura).
'''

temp = float(input())

if temp <= -20:
    print("Muito Baixa")
elif temp <= 30:
    print("Baixa")
elif temp <= 200:
    print("Normal")
elif temp <= 250:
    print("Alta")
else:
    print("Muito Alta")