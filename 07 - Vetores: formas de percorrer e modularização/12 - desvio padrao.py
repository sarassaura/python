'''
Faça um programa que calcule o desvio padrão (σ) 
de um vetor v contendo n elementos reais, 
em que μ é a média do vetor.

σ = (1/(n−1) * ∑(n−1,i=0) (v[i]−μ)^2)^(0.5)

Seu programa deve primeiramente solicitar o valor n e 
depois realizar a leitura dos valores de v. 
A saída será: "O desvio padrão vale D.", 
em que D deve ser formatado com duas casas decimais.

Importante: Neste exercício, 
não é permitido usar funções prontas em listas. 
Por exemplo: min, max, del, in, sort, reverse, index, count, etc.
'''

n = int(input())
v = [0] * n
mi = 0

for x in range(n):
    v[x] = float(input())
    mi += v[x]

mi /= n

sum = 0

for x in range(n):
    sum += (v[x] - mi)**2

D = ((1/(n-1)) * sum)**0.5

print("O desvio padrão vale {:.2f}.".format(D))