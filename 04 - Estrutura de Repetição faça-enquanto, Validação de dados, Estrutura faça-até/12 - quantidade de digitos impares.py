'''
Escreva a função qtd_digitos_impares que 
recebe um valor inteiro n. 
A função deverá retornar a 
quantidade de dígitos ímpares no número n. 
Por exemplo, o número 12345 possui 
três dígitos ímpares (1, 3 e 5). 
Neste caso, a função deveria retornar o valor 3.

Entrada:

    n

Saída:

    Quantidade de dígitos ímpares (retorno da função submetida)

'''

def qtd_digitos_impares(n):
    odd = 0
    
    for x in range(len(str(n))):
        if((n % 10) % 2 == 1):
            odd += 1
        n = n // 10
    return odd