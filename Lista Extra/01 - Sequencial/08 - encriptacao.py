'''
Um determinado método para encriptar números de 
4 dígitos consiste em adicionar 1 em 
cada dígito do número. Por exemplo:

    O número 1234 ficaria 2345 após a encriptação;
    O número 9092 ficaria 0103 após a encriptação.

Entrada:

    Número a ser encriptado

Saída:

    Número encriptado

'''

n = int(input())
result = ""

for x in str(n):
    result += str((int(x) + 1) % 10)

print(result)