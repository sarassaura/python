'''
A distância de Manhattan entre os pontos (x1, y1) e (x2, y2) é definida da seguinte forma:

∣x2−x1∣+∣y2−y1∣

Escreva uma função/método para calcular a distância de Manhattan. 
A função/método  possui os parâmetros x1, y1, x2, y2 (números inteiros) 
e deverá retornar o valor da distância de Manhattan 
entre os pontos (x1, y1) e (x2, y2).

Função/método a ser implementado:

Python (o arquivo submetido deve ter a extensão .py):

def calcular_distancia(x1, y1, x2, y2):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static int calcularDistancia(int x1, int y1, int x2, int y2) {
    // codigo do metodo
}

Entrada:

    x1
    y1
    x2
    y2

Saída:

    Distância de Manhattan (retorno da função/método)

'''

def calcular_distancia(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2-y1)