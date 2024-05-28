'''
Um número pentagonal é um número poligonal que 
é uma extensão do conceito de números triangulares e 
números quadrados para o pentágono, mas, 
diferentemente desses outros dois, 
o processo que envolve a construção dos 
números pentagonais não é uma simetria rotacional.

Porém, há uma fórmula recursiva que pode ser usada para 
o cálculo da sequência de números pentagonais. 
Assim, dado que P(1) = 1,

P(n) = P(n-1) + (3(n-1) + 1),  para n ≥ 2

Com isso, P(2) = P(1) + (3 x (2 - 1) + 1) = 1 + 4 = 5

                 P(3) = P(2) + (3 x (3 - 1) + 1) = 5 + 7 =12

                 P(4) = P(3) + (3 x (4 - 1) + 1) = 12 + 10 = 22

                 E assim sucessivamente.


Faça um programa que receba um valor inteiro n 
e imprima a sequência dos n primeiros 
números pentagonais, separados por um espaço.

Exemplo:

Entrada:
5

Saída:
1 5 12 22 35
'''

number = int(input())
result = "1"
before = 1
now = 1

for x in range(number - 1):
  now = before + ((3 * (x + 1)) + 1)
  result += " " + str(now)
  before = now

print(result)