'''
Sabe-se que o volume (V) de uma esfera pode ser calculado usando a formulação

V = 4/3 * π * r^3

em que r é o raio da esfera.

Escreva uma função chamada volume_esf que 
receba como parâmetro o raio de uma esfera e retorne seu volume. 

Para a utilização do valor de π sua função deve fazer uso da biblioteca math, 
com o comando math.pi.
'''

import math

def volume_esf(r):
    return (4 / 3) * math.pi * pow(r, 3)