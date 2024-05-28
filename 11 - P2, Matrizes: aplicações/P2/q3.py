'''
Um quadrado mágico é uma matriz quadrada sem elementos repetidos, 
em que a soma de qualquer uma das linhas é igual à 
soma de qualquer uma das colunas, que também é igual à 
soma da diagonal principal e da diagonal secundária.

A matriz abaixo é um exemplo de quadrado mágico com dimensão 3, 
pois não há valores repetidos e a somatória, 
em todos os casos (linhas, colunas ou diagonais), é igual a 15.

4	9	2
3	5	7
8	1	6

Escreva uma função quadrado_magico, que recebe uma matriz quadrada de 
números inteiros não repetidos M e retorna uma variável booleana e 
o valor da soma (das linhas, colunas ou diagonais). 
A variável booleana deve ter valor True se a matriz de entrada é 
um quadrado mágico e False se a matriz não é um quadrado mágico. 
Para o exemplo da matriz acima, o retorno da função terá a 
variável booleana com valor True e um número inteiro igual a 15 para a soma.

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, entre outras.

Dica: comece obtendo a soma de uma das linhas, colunas ou diagonais (você pode escolher). 
Depois, compare a soma obtida com as somas de cada linha, coluna ou diagonais restantes.
'''

def quadrado_magico(M):
  magic = True
  soma = 0

  n = len(M)

  for x in range(n):
    soma += M[0][x]

  main = 0
  sup = 0

  for i in range(n):
    linha = 0
    coluna = 0
    for j in range(n):
      linha += M[i][j]
      coluna += M[j][i]
    if linha != soma or coluna != soma:
      return False,soma
  
  for y in range(n):
    main += M[y][y]

  if main != soma:
    return False,soma

  for z in range(n):
    sup += M[z][n - 1 - z]

  if sup != soma:
    return False,soma

  return magic,soma