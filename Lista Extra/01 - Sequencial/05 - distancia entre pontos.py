'''
Sejam A e B dois pontos quaisquer no plano cartesiano, 
representados por um par de coordenadas (x, y). 
A menor distância entre A e B é um segmento de reta 
que tem os dois pontos como extremidade.

Representando as coordenadas de A pelo 
par(Ax,Ay), e as coordenadas de B pelo 
par (Bx, By), podemos calcular essa 
distância pela equação:

d(AB)=√(Bx−Ax)^2+(By−Ay)^2

Escreva um programa que receba as coordenadas de dois pontos 
A e B e calcule a distância entre eles.

Entrada:
A entrada consiste de 4 números reais na seguinte ordem:
    
Ax

Ay

Bx

By

Saída:

    Seu programa deve imprimir na tela, com duas casas decimais, a distância entre os pontos.
'''

ax = float(input())
ay = float(input())
bx = float(input())
by = float(input())

distancia = ((bx - ax)**2 + (by- ay)**2)**0.5

print("{:.2f}".format(distancia))