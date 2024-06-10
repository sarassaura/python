'''
Faça um programa que, dados os coeficientes 
a,b,c , resolva a equação de segundo grau:

ax^2+bx+c=0

    Caso a equação não tenha solução, 
    o programa deverá exibir "Sem solucao real!", 
    seguido pelo valor de Δ, formatado com duas casas decimais.
    Caso a equação tenha solução única, 
    o programa deverá exibir apenas essa solução, 
    formatada com duas casas decimais.
    Caso a equação tenha duas soluções, 
    o programa deverá exibi-las em linhas separadas, 
    em ordem crescente, formatadas com duas casas decimais.


Entradas:

    Coeficiente a (inteiro)
    Coeficiente b (inteiro)
    Coeficiente c (inteiro)

Saídas:

    Soluções de ax^2+bx+c=0

    (se existirem)


Observações:
1. Nexte exercício, pode utilizar funções prontas para calcular raiz quadrada.

    Em Java:

import java.lang.Math;
double resultado = Math.sqrt(9)

    Em Python:

import math
resultado = math.sqrt(9)


2. Formatação da saída:
Em Python, é possível formatar saídas das seguintes formas:

a = 3.14159
b = 2.71828
print("a vale %.2f e b vale %.3f" % (a, b))
print("a vale {:.2f} e b vale {:.3f}".format(a, b))

Em Java, é possível formatar saídas das seguintes formas:

double a = 3.14159;
double b = 2.71828;
System.out.printf("a vale %.2f e b vale %.3f\n", a, b);
System.out.println(String.format("a vale %.2f e b vale %.3f", a, b));



Exemplo 1:
Entradas:

1
2
3

Saídas:

Sem Solucao real!
Delta = -8.00


Exemplo 2:
Entradas:

4
-4
1

Saídas:

x = 0.50


Exemplo 3:
Entradas:

2
5
-4

Saídas:

x1 = -3.14
x2 = 0.64
'''

a = int(input())
b = int(input())
c = int(input())

delta = (b**2) - (4 * a * c)

if delta < 0:
    print("Sem solucao real!")
    print("Delta = {:.2f}".format(delta))
elif delta == 0:
    print("x = {:.2f}".format(-b/(2*a)))
else:
    x1 = (-b + (delta)**0.5) / (2 * a)
    x2 = (-b - (delta)**0.5) / (2 * a)
    if x2 < x1:
        temp = x1
        x1 = x2
        x2 = temp
    print("x1 = {:.2f}".format(x1))
    print("x2 = {:.2f}".format(x2))