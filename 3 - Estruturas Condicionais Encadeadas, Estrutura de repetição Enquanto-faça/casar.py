'''
Elabore um algoritmo para resolver o fluxograma a seguir:

Image: https://drive.google.com/file/d/1MH8fIMbSEOoKQ7Fm9311T7ZNYp4s6yPh/view?usp=drive_link

Os seguintes testes serão realizados,   

ENTRADA 1:

SIM
SIM

SAÍDA 1:

COMPRE UMA BICICLETA

ENTRADA 2:

SIM
NAO

SAÍDA 2:

CASE

ENTRADA 3:

NAO
NAO

SAÍDA 3:

COMPRE UMA BICICLETA

ENTRADA 4:

NAO
SIM

SAÍDA 4:

CASE
'''

gordo = input()

if gordo == "SIM":
    emagrecer = input()
    if emagrecer == "SIM":
        print("COMPRE UMA BICICLETA")
    else:
        print("CASE")
else:
    engordar = input()
    if engordar == "SIM":
        print("CASE")
    else:
        print("COMPRE UMA BICICLETA")