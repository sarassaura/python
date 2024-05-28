'''
Para determinadas aplicações, a descrição de coordenadas 
geográficas em graus decimais (GD) ou 
em grau, minuto, segundo (GMS) pode ser mais adequada. 
Como no sistema de medida de tempo, 
no sistema GMS  1 grau é dividido em 60 minutos. 
O minuto, por sua vez, é dividido em 60 segundos.

Para este programa, 
você deve escrever o código para duas funções, 
chamadas gd2gms e gms2gd, cujos protótipos estão disponíveis. 

A primeira função, gd2gms, 
recebe como entrada um único parâmetro: 
um número real que representa graus decimais. 
A função converte esse número para o sistema GMS, 
retornando três parâmetros, nesta ordem: 
grau (número inteiro), minuto (número inteiro) e segundo (número real). 
Não se preocupe com a formatação da saída! 
Apenas retorne os três parâmetros, nesta ordem.

A segunda função, gms2gd, recebe como entrada três parâmetros, 
nesta ordem: um número inteiro (representando graus), 
um número inteiro (representando minutos) e 
um número real (representando segundos). 
A função converte esse número para o sistema GD e 
retorna apenas um número real, representando graus decimais. 
Não se preocupe com a formatação da saída! 
Apenas retorne o parâmetros.

Exemplos de saídas esperadas:

Para gd2gms com entrada igual a 23.678:

Saída:
23
40
40.80

Para gms2gm com entrada 56; 45; 56.88:

Saída:
56.7658
'''

def gd2gms(gd):
    graus = int(gd)
    minutos = int((gd - graus) * 60)
    segundos = (gd - graus - (minutos / 60)) * 3600
    return graus, minutos, segundos

def gms2gd(g,m,s):
    result = g + (m / 60) + (s / 3600)
    return result