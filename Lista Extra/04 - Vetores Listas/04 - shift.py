'''
Implemente:

a) Uma função/método (inserir) que leia (Scanner/input) 10 valores 
inteiros e insira esses elementos em um vetor (a função/método 
retorna (return) esse vetor preenchido com 10 inteiros);
b) Uma segunda função/método (imprimir) que receba o vetor 
criado em (a) e imprima os seus elementos (inclua um caractere 
espaço entre cada elemento impresso; quebre uma linha após a impressão do último elemento);
c) Uma terceira função/método (shift) que receba o vetor criado em 
(a) e faça um shift para a direita em cada elemento inserido no vetor. 
Além disso, o vetor  deve ser circular, ou seja, o valor da última 
posição deve ser o valor da primeira. Por exemplo,

Vetor original: [2, 4, 1, 5, 2, 18, 9, 3, 5, 10]
Vetor após shift: [10, 2, 4, 1, 5, 2, 18, 9, 3, 5] 


Funções/métodos a serem implementados:

Python (o arquivo submetido deve ter a extensão .py):

def inserir():
    #código da função

def imprimir(v):
    #código da função

def shift(v):
    #código da função


Java (o arquivo submetido deve ter a extensão .java):

import java.util.Scanner;

public static int[] inserir() {
    //código do método
}

public static void imprimir(int[] v) {
    //código do método
}

public static void shift(int[] v) {
    //código do método
}

Neste exercício, não é permitido utilizar:

    Em Java: as classes Arrays, Collections, Vector, ArrayList e LinkedList.
    Em Python: as funções de listas: del, append, extend, insert, remove, pop.

Entrada:

    10 valores inteiros (elementos do vetor)

Saída:

    Elementos do vetor lido
    Elementos do vetor após o shift

Python:

v = inserir()
imprimir(v)
shift(v)
imprimir(v)

Java:

int[] v = Modulo.inserir();
Modulo.imprimir(v);
Modulo.shift(v);
Modulo.imprimir(v);


Exercício adaptado de Prof. Wagner Tanaka Botelho - Processamento da Informação 2022
'''

def inserir():
    vec = [0,0,0,0,0,0,0,0,0,0]
    for x in range(10):
        vec[x] = int(input())
    return vec


def imprimir(v):
    a = str(v[0])
    for x in range(1,10):
        a += " " + str(v[x])
    print(a)

def shift(v):
    a = [0,0,0,0,0,0,0,0,0,0]
    a[0] = v[9]
    for x in range(9):
        a[x + 1] = v[x]
    for x in range(10):
        v[x] = a[x]