'''
O valor de Π

pode ser calculado pela série de Gregory conforme apresentado a seguir:

Π/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9...


Escreva a função calcular_pi que recebe o parâmetro n e retorne o valor de Π
usando n elementos da série de Gregory. Use apenas a estrutura de repetição while.

Entrada:

    n

Saída:

    Valor de Π
'''

def calcular_pi(n):
    result = 0
    j = 1
    k = 1

    while n > 0:

        result += j / k

        j *= -1
        k += 2
        n -= 1
    
    return result * 4