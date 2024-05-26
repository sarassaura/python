'''
Sabe-se que a partir de dois pontos no espaço bidimensional (x1,y1) e (x2,y2),
pode-se calcular a Distância Euclidiana entre eles
a partir da construção de um triângulo retângulo, 
em que os catetos são  c1 =|x1 - x2| e  c2 =|y1 - y2|. 
A Distância Euclidiana (d) entre os pontos é obtida 
pelo cálculo da hipotenusa do triângulo retângulo:

d=((x1-x2)^2+(y1-y2)^2)^(1/2)

Escreva uma função chamada dEuclidiana que 
receba como parâmetros x1, y1, x2 e y2 e 
retorne a distância Euclidiana entre os pontos.

Para a utilização calcular a raiz quadrada 
você pode usar o camando sqrt da biblioteca numpy.
'''

def dEuclidiana(x1, y1, x2, y2):
    return pow((pow(x1 - x2, 2) + pow(y1 - y2, 2)),0.5)