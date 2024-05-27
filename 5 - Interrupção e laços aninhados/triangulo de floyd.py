'''
Escreva um programa que leia um número inteiro positivo N e 
em seguida imprima N linhas do chamado triângulo de Floyd. 
Por exemplo, para N=6, o seguinte triângulo é formado:

1
2     3
4     5     6
7     8     9     10
11    12    13    14    15
16    17    18    19    20    21

Dica:
Entre os números, há quatro (4) caracteres espaço.

Os seguintes testes serão executados:

ENTRADA 1:

6

SAÍDA:

1
2     3
4     5     6
7     8     9     10
11    12    13    14    15
16    17    18    19    20    21

ENTRADA 2:

3

SAÍDA:

1
2    3
4    5    6
ENTRADA 3:


10

SAÍDA:

1
2     3
4     5     6
7     8     9     10
11    12    13    14    15
16    17    18    19    20    21
22    23    24    25    26    27    28
29    30    31    32    33    34    35    36
37    38    39    40    41    42    43    44    45
46    47    48    49    50    51    52    53    54    55
'''

N = int(input())
digits = 1
count = 1

for x in range(N):
    line = ""
    count += x
    for y in range(digits):
        line += str(y + count) + "    "
    print(line)
    digits += 1