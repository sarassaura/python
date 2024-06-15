'''
Escreva uma função/método que recebe duas matrizes (matriz1 e matriz2) 
e retorne True caso a matriz2 tenha todos os valores duplicados nas 
posições correspondentes da matriz1. Caso contrário, deve-se retornar False. 
Se as dimensões da matriz1 forem diferentes das dimensões da matriz2, 
a função deve retornar False.

Por exemplo, a função deve retornar True para as duas matrizes a seguir:

11 22
33 44

22 44
66 88


Função/método a ser implementado:

Python (o arquivo submetido deve ter a extensão .py):

def comparar_matrizes(matriz1, matriz2):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static boolean compararMatrizes(int[][] matriz1, int[][] matriz2) {
    // codigo do metodo
}

Neste exercício, não é permitido utilizar:

    Em Java: as classes Arrays, Collections, Vector, ArrayList e LinkedList.
    Em Python: as funções de listas: del, append, extend, insert, remove, pop.

Entrada:

    número de linhas e número de colunas da matriz1
    elementos da matriz1
    número de linhas e número de colunas da matriz2
    elementos da matriz2

Saída:

    retorno da função/método
'''

def comparar_matrizes(matriz1, matriz2):
    l1 = len(matriz1)
    c1 = len(matriz1[0])
    l2 = len(matriz2)
    c2 = len(matriz2[0])

    if l1 != l2 or c1 != c2:
        return False

    for x in range(l1):
        for y in range(c1):
            if matriz2[x][y] != matriz1[x][y] * 2:
                return False

    return True
