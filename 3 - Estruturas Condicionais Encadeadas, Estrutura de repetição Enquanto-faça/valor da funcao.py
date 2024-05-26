'''
f(a,b,c) = a + ∑(b,d=1) c * d


Escreva a função obter_valor_funcao que possui os parâmetros 
a, b, c (nesta ordem) e retorne o resultado de f(a, b, c). 
Sua função deve usar a estrutura de repetição while.

Entrada:

    a
    b
    c

Saída:

    Valor da função (retorno da função submetida)
'''

def obter_valor_funcao(a, b, c):

  D = 1
  somatorio = 0

  while D <= b:
    somatorio += c * D
    D += 1

  soma = somatorio + a

  return soma