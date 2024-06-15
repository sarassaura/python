'''
Implemente a função/método intercalar. Essa função/método recebe dois vetores (v1 e v2) com 5 números cada do tipo inteiro. Após isso, um terceiro vetor (v3)  deve ser retornado com os elementos de v1 e v2 intercalados.

Para melhor compreender como a função/método intercalar(v1, v2) deve ser implementada considere o seguinte exemplo:

v1 = [1, 2, 3, 4, 5]
v2 = [4, 5, 6, 7, 8]

Nesse exemplo, a função/método deve retornar v3 com os seguintes elementos:

v3 = [1, 4, 2, 5, 3, 6, 4, 7, 5, 8]


Função/método a ser implementado:

Python (o arquivo submetido deve ter a extensão .py):

def intercalar(v1, v2):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static int[] intercalar(int[] v1, int[] v2) {
    // codigo do metodo
}

Neste exercício, não é permitido utilizar:

    Em Java: as classes Arrays, Collections, Vector, ArrayList e LinkedList.
    Em Python: as funções de listas: del, append, extend, insert, remove, pop.

Entrada:

    5 valores inteiros (elementos de v1)
    5 valores inteiros (elementos de v2)

Saída:

    Elementos de v1
    Elementos de v2
    Elementos do vetor retornado pela função/método
'''

def intercalar(v1, v2):
    v3 = [0,0,0,0,0,0,0,0,0,0]

    for x in range(5):
        v3[x * 2] = v1[x]
        v3[(x * 2) + 1] = v2[x]

    return v3