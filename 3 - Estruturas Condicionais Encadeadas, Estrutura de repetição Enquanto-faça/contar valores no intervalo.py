'''
Escreva um programa, usando a estrutura de repetição while, para ler N valores reais e 
determinar quantos destes estão no intervalo fechado [10, 20]. 
Seu programa deve primeiramente receber o valor N.

A saída do programa deve ser: 
"Tem v valores no intervalo [10,20].", 
em que v é a quantidade de valores encontrada.
'''

N = int(input())
count = 0
v = 0

while count < N:
  A = float(input())
  if A >= 10 and A <= 20:
    v += 1
  count += 1

print("Tem {:d} valores no intervalo [10,20].".format(v))