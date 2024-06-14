'''
f(a,b,c) = a + ∑(b, d=1) (c * d)


Escreva uma função/método para a obter o valor da função na equação presentada. 
Essa função/método possui os parâmetros a, b, c (nesta ordem) e deve retornar 
o resultado de f(a, b, c).


Python (o arquivo submetido deve ter a extensão .py):

def obter_valor_funcao(a, b, c):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static int obterValorFuncao(int a, int b, int c) {
    // codigo do metodo
}

Entrada:

    a
    b
    c

Saída:

    Valor da função (retorno da função submetida)
'''

def obter_valor_funcao(a, b, c):
    d = 1
    sum = 0
    while d <= b:
        sum += c * d
        d += 1 
    return a + sum