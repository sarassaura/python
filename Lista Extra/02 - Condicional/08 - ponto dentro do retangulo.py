'''
Escreva um programa que leia os valores x e y de um ponto. 
A partir disso, determine se o ponto está dentro ou fora do retângulo a seguir:

https://drive.google.com/file/d/1pp09BoKDTL2QmItbyVeZ_dsGWecbyEGW/view?usp=drive_link

Entrada:

    x
    y

Saída:

Imprima "SIM", caso o ponto esteja dentro do retângulo; 
ou, caso contrário, imprima "NAO".
'''

x = int(input())
y = int(input())

if x >= -800 and x <= 22 and y >= -20 and y <= 35:
    print("SIM")
else:
    print("NAO")