'''
Este exercício é uma continuação do anterior e você deve partir da 
implementação da função que você desenvolveu no exercício anterior, 
promovendo o ataque de sistema.

Agora, você deve implementar (a partir do que você já fez) 
uma estratégia de jogadas para o sistema se 
nenhum jogador (você ou o sistema) tem a 
oportunidade de ganhar na próxima jogada. 

Esta estratégia deve seguir o seguinte conjunto de regras:

    O sistema deve sempre priorizar a ocupação dos cantos do quadro, 
    desde que o adversário ainda não tenha ocupado nenhum deles;
    Se o adversário já tiver ocupado qualquer um dos cantos, 
    a prioridade da jogada deve mudar para a ocupação do meio do quadro, 
    desde que este esteja livre. Com o meio do quadro ocupado, 
    a prioridade deve continuar sendo ocupar os cantos.
    A partir do momento em que todos os cantos estiverem ocupados por 
    qualquer adversário, o sistema deve sortear a próxima jogada em 
    função das opções existentes.

Assim como no exercício anterior, a função desenvolvida será chamada por 
um programa principal, que primeiramente lerá uma matriz de testes com 
o estado atual do jogo, bem como as marcas dos jogadores. 
Sua função não deve ler (input) nem imprimir (print) nada! 
Tudo isso será feito pelo programa principal ao qual vocês não têm acesso. 
Para cada teste, será assumido que é a vez do sistema computacional jogar.

Importante: Neste exercício, não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, entre outras. 

Teste sua função, na prática, substituindo a função original 
jogadaSistema e tente ganhar dos sistema!
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
        cantos = []
        meio = []
        canto_oposto = True

        if matrizS[0][0] == suaMarca:
            canto_oposto = False
        if matrizS[0][(len(matrizS) - 1)] == suaMarca:
            canto_oposto = False
        if matrizS[(len(matrizS) - 1)][0] == suaMarca:
            canto_oposto = False
        if matrizS[(len(matrizS) - 1)][(len(matrizS) - 1)] == suaMarca:
            canto_oposto = False        
        for x in range(len(opcoes)):
            op = opcoes[x]
            if op[0] == 0 and op[1] == 0:
                cantos.append(op)
            if op[0] == 0 and op[1] == (len(matrizS) - 1):
                cantos.append(op)
            if op[0] == (len(matrizS) - 1) and op[1] == 0:
                cantos.append(op)
            if op[0] == (len(matrizS) - 1) and op[1] == (len(matrizS) - 1):
                cantos.append(op)
            if op[0] == ((len(matrizS) - 1) / 2) and op[1] == ((len(matrizS) - 1) / 2):
                meio.append(op)
        if len(cantos) == 0:
            pos = np.random.randint(len(opcoes), dtype=int)
            jogada = opcoes[pos]
            return jogada                
        if canto_oposto:
            return cantos[0]
        if len(meio) > 0:
            return meio[0]
        return cantos[0]