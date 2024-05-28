'''
Modifique a função jogadaSistema, apresentada nesta aula, 
de forma que o sistema computacional com o qual 
você está jogando não apenas se defenda, 
mas também ataque quando tiver a oportunidade. 
A nova função receberá, além da marca com a qual 
você está jogando (chamada de suaMarca no programa), 
a marca com a qual o sistema computacional está 
jogando (outraMarca no programa).  

Além disso, a biblioteca em que a função será implementada importa, 
além da biblioteca numpy, funções importantes para a 
implementação do jogo da velha como opcoesDeJogada e avaliaSeVencedor. 
Estas funções foram colocadas em uma biblioteca chamada mybib, 
que também contém outras funções como avaliaLinhas, avaliaColunas, 
avaliaDiagonalPrincipal e avaliaDiagonalSecundaria. 

A biblioteca funcao.py ainda seta o gerador de números aleatórios 
com um seed de 667, de modo que qualquer computador reproduza 
a mesma sequência de números. 

A primeira providência para construir a nova função é verificar 
se o sistema pode vencer na próxima jogada (verificação de ataque). 
Caso afirmativo, o sistema deve jogar para vencer. Caso contrário, 
o sistema deve verificar a possibilidade de você vencer na próxima jogada e,
caso afirmativo, bloquear sua possibilidade de vitória. 
Esse comportamento reativo já está presente no código atual. 
Caso ninguém possa vencer, o sistema deve sortear uma posição para jogar, 
nos mesmos moldes do que é feito no código atual.

A função desenvolvida será chamada por um programa principal, 
que primeiramente lerá uma matriz de testes com o estado atual do jogo, 
bem como as marcas dos jogadores. Sua função não deve ler (input) 
nem imprimir (print) nada! Tudo isso será feito pelo programa principal 
ao qual vocês não têm acesso. Para cada teste, será assumido que 
é a vez do sistema computacional jogar.

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, entre outras. 

Teste sua função, na prática, substituindo a 
função original jogadaSistema e tente ganhar dos sistema!
'''

import numpy as np
np.random.seed(667)
from mybib import opcoesDeJogada, avaliaSeVencedor

def jogadaSistema(matrizS, suaMarca, outraMarca):
    resp = False
    opcoes = opcoesDeJogada(matrizS)
    defesas = []
    ataques = []

    for i in range(len(opcoes)):
        op = opcoes[i]
        s_copy = [[v for v in r] for r in matrizS]
        s_copy[op[0]][op[1]] = suaMarca
        resp, c = avaliaSeVencedor(s_copy)
        if resp == True:
            defesas.append(op)

    for i in range(len(opcoes)):
        op = opcoes[i]
        s_copy = [[v for v in r] for r in matrizS]
        s_copy[op[0]][op[1]] = outraMarca
        resp, c = avaliaSeVencedor(s_copy)
        if resp == True:
            ataques.append(op)

    if len(ataques) > 0 or len(defesas) > 0:
        resp = True

    if resp == True:
        if len(ataques) == 0 and len(defesas) > 0:
            return defesas[0]
        if len(ataques) > 0 and len(defesas) == 0:
            return ataques[0]
        if len(ataques) > 0 and len(defesas) > 0:
            for x in range(len(ataques)):
                for y in range(len(defesas)):
                    if ataques[x] == defesas[y]:
                        return ataques[x]
            return ataques[0]

    if (resp == False):
        pos = np.random.randint(len(opcoes), dtype=int)
        jogada = opcoes[pos]
        return jogada