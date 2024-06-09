'''
Escreva a função somar_vizinhos que recebe uma matriz e 
os índices de uma célula (linha, coluna). 
A função deve retornar o valor da soma das células vizinhas. 
Observe que linha e coluna iniciam no valor zero.

Por exemplo, para a matriz com linha=2 e coluna=3, 
a função somar_vizinhos deve retornar o valor 20 
(3+1+1+2+2+1+5+5).

1 	2 	3 	4 	5 	6 	7
2 	1 	3 	1 	1 	0 	0
3 	1 	2 	2 	2 	1 	0
1 	0 	1 	5 	5 	1 	1
1 	1 	1 	0 	1 	0 	0


Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, entre outras.
'''

def somar_vizinhos(matriz, linha, coluna):
    sum = 0

    for x in range(linha - 1, linha + 2):
        if x < 0:
            continue
        for y in range(coluna - 1, coluna + 2):
            if y < 0:
                continue
            try:
                sum += matriz[x][y]
            except:
                pass
    
    return sum - matriz[linha][coluna]