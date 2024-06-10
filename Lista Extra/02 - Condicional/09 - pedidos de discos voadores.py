'''
Uma montadora de discos voadores possui fábricas em diversos planetas e 
faz entregas em diversas partes do universo. Essa empresa usa números de 
6 dígitos para identificar a origem do disco, o destino do disco e o modelo, 
conforme formato a seguir:

OODDMM:

    OO: código do planeta de origem (onde o disco voador foi fabricado)
    DD: código do planeta de destino (onde o disco voador será entregue)
    MM: código do modelo

A empresa usa as seguintes tabelas com os códigos de planetas e modelos de discos voadores:

************************
* Código  *  Planeta   *
*  80 	  *  Marte     *
*  81 	  *  Saturno   *
*  90 	  *  Netuno    *
*  91 	  *  HD21749b  *
************************

**********************
*  Código  *  Modelo *
*    60    *  A6000  *
*    61    *  B7500  *
*    62    *  C9000  *
**********************

Portanto, o número 809162 será usado para um disco voador 
fabricado em Marte (código 80), 
entregue em HD21749b (código 91) 
e do modelo C9000 (código 62).

Escreva um programa que leia um número de 6 dígitos e 
então imprima o planeta de origem, o planeta de destino e o modelo.

Entrada

    Número de 6 dígitos


Saída

    Planeta de origem
    Planeta de destino
    Modelo do disco voador
'''

cod = int(input())

def planeta(s):
    if s == "80":
        return "Marte"
    elif s == "81":
        return "Saturno"
    elif s == "90":
        return "Netuno"
    elif s == "91":
        return "HD21749b"
    
def modelo(s):
    if s == "60":
        return "A6000"
    elif s == "61":
        return "B7500"
    elif s == "62":
        return "C9000"
    
origem = str(cod)[slice(0,2)]
destino = str(cod)[slice(2,4)]
disco = str(cod)[slice(4,6)]

print(planeta(origem))
print(planeta(destino))
print(modelo(disco))