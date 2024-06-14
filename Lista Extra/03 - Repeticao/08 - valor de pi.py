'''
O valor de Π

pode ser calculado pela série de Gregory conforme apresentado a seguir:

Π / 4= 1/1 − 1/3 + 1/5 − 1/7 + 1/9...


Escreva uma função/método para calcular o valor de Π
. A função/método recebe o parâmetro n e retorna o valor de Π

usando n elementos da série de Gregory.


Python (o arquivo submetido deve ter a extensão .py):

def calcular_pi(n):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static double calcularPi(int n) {
    // codigo do metodo
}

Entrada:

    n

Saída:

    Valor de Π

(retorno da função submetida)
'''

def calcular_pi(n):
    sum = 0
    div = 1
    top = 1
    for x in range(n):
        sum += top / div
        div += 2
        top *= -1
    return sum * 4