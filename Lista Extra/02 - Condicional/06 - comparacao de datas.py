'''
Escreva uma função/método para comparar duas datas. 
A função/método possui os parâmetros d1, m1, a1, d2, m2, a2 
(números inteiros representando o dia(d), mês(m) e ano(a) da data1 e da data2) 
e deverá retornar um valor inteiro conforme definido a seguir:

    Retorna -1 se a data1 é a mais antiga;
    Retorna 0 se as duas datas são iguais;
    Retorna 1 se as data2 é a mais antiga.

Função/método a ser implementado:

Python (o arquivo submetido deve ter a extensão .py):

def comparar_datas(d1, m1, a1, d2, m2, a2):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static int compararDatas(int d1, int m1, int a1, int d2, int m2, int a2) {
    // codigo do metodo
}

Entrada:

    d1
    m1
    a1
    d2
    m2
    a2

Saída:

    Retorno da função/método submetida
'''

def equal_length(x):
    if len(str(x)) == 1:
        return "0" + str(x)
    else:
        return str(x)

def comparar_datas(d1, m1, a1, d2, m2, a2):

    data1 = str(a1) + equal_length(m1) + equal_length(d1)
    data2 = str(a2) + equal_length(m2) + equal_length(d2)
    
    if data1 == data2:
        return 0
    elif int(data1) > int(data2):
        return 1
    else:
        return -1