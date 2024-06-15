'''
Escreva uma função/método que recebe um valor n (assuma que n é impar). 
A função/método deve retornar uma matriz X, formada por números 1 nas 
diagonais e 0 em todas as outras posições.

Por exemplo, para n=5, a função deve retornar a seguinte matriz:

1 	0 	0 	0 	1
0 	1 	0 	1 	0
0 	0 	1 	0 	0
0 	1 	0 	1 	0
1 	0 	0 	0 	1

Função/método a ser implementado:

Python (o arquivo submetido deve ter a extensão .py):

def obter_matriz_x(n):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static int[][] obterMatrizX(int n) {
    // codigo do metodo
}

Neste exercício, não é permitido utilizar:

    Em Java: as classes Arrays, Collections, Vector, ArrayList e LinkedList.
    Em Python: as funções de listas: del, append, extend, insert, remove, pop.

Entrada:

    n

Saída:

    retorno da função/método

Exercício adaptado de Gabriel Ângelo Sembenelli (2022).
'''

def obter_matriz_x(n):
    m = [[1 if ((i == j) or (i + j == n - 1)) else 0 for i in range(n)]
         for j in range(n)]

    return m
