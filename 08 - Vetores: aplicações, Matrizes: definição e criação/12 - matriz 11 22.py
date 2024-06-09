'''
Escreva a função criar_matriz que recebe os parâmetros 
n_linhas e n_colunas e retorne uma matriz com dimensões 
n_linhas x n_colunas. Na primeira metade da matriz, 
as linhas são preenchidas com o valor 11 e 
a segunda metade com o valor 22. Por exemplo, 
para n_linhas=4 e n_colunas=4, 
a seguinte matriz deve ser retornada:

11 11 11 11
11 11 11 11
22 22 22 22
22 22 22 22

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, entre outras. 
Além disso, submeta APENAS a função criar_matriz(n_linhas, n_colunas) e 
não realize leitura de dados (input) ou impressão de dados na função (print).


Desafio: Você consegue usar compreensão de listas e 
criar a matriz, conforme requerida, usando apenas uma linha de código?
'''

def criar_matriz(n_linhas, n_colunas):
    m = [[11 if j <= ((n_linhas - 1) // 2) else 22 for i in range(
        n_colunas)] for j in range(n_linhas)]
    return m
