'''
Implemente a função intercalar() que 
RECEBE DOIS vetores (v_1 e v_2) com 
5 números CADA do tipo inteiro. 
Após isso, um terceiro vetor (v_3) 
deve ser RETORNADO com 
os elementos de v_1 e v_2 INTERCALADOS. 

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, 
index, count, entre outras. 

Não use a função append neste exercício.

Para melhor compreender como a função intercalar(v_1, v_2) 
deve ser implementada, por exemplo, se:

v_1 = [1, 2, 3, 4, 5]
v_2 = [4, 5, 6, 7, 8]

A função deve retornar v_3 com os seguintes elementos:

v_3 = [1, 4, 2, 5, 3, 6, 4, 7, 5, 8]
'''

def intercalar(v_1, v_2):
    v = [0] * 10

    for x in range(10):
        if x % 2 == 0:
            v[x] = v_1[int(x / 2)]
        else:
            v[x] = v_2[int((x - 1) / 2)]

    return v