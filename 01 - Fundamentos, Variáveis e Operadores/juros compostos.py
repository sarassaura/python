'''
O gerente de uma empresa está planejando realizar um investimento, 
mas ele precisa de um programa para calcular o valor que ele obterá após um determinado período.

Escreva um programa que lerá o valor do investimento inicial, 
a taxa de juros anual e o período que o valor ficará investido (em anos). 
A taxa de juros é recebida como um número fracionário, portanto, 
o valor 0.10 siginifica uma taxa de juros de 10% ao ano. 
O programa deve imprimir:

    Valor do investimento inicial
    Taxa de juros
    Tempo
    Valor total após o período (valor do investimento mais os rendimentos obtidos no período)

A impressão deve ser realizada no seguinte formato 
(obverse que números fracionários devem ser impressos com duas casas decimais):

Valor = 100.00
Taxa de juros = 0.10
Tempo = 1
Valor apos o periodo = 110.00

Observação: para formatar a saída com duas casas decimais em Python é possível utilizar o seguinte código:

numero = 5.07507
print("Valor = {:.2f}".format(numero))


Fórmula para calcular juros compostos:

total=inicial*(1+taxa)^tempo


Formato do caso de teste: esse é o formato dos casos de teste que aparecem ao avaliar a atividade.

Entrada:

    valor do investimento inicial
    taxa de juros (anual)
    período (em anos)

Saída:

    dados do investimento conforme formato especificado no enunciado
'''

print('Digite o investimento inicial:')
investimento_inicial = float(input())
print('Digite a taxa de juros anual (0 à 1):')
taxa_juros_anual = float(input())
print('Digite o período em anos:')
periodo_anos = float(input())

print()

total = investimento_inicial * pow((1 + taxa_juros_anual),periodo_anos)

print('Valor = {:.2f}'.format(investimento_inicial))
print('Taxa de juros = {:.2f}'.format(taxa_juros_anual))
print('Tempo =', int(periodo_anos))
print('Valor apos o periodo = {:.2f}'.format(total))