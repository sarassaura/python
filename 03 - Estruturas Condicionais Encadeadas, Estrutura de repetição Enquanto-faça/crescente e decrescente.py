'''
Faça um programa, usando a estrutura de repetição while, 
que leia um número inteiro positivo N e 
imprima todos os números naturais de 0 até N em ordem CRESCENTE em uma linha. 
Depois, imprima esses números em ordem DECRESCENTE em outra linha. 
Inclua um caractere espaço entre cada número impresso.

Dica 1: para imprimir a saída na mesma linha, é necessário especificar o parâmetro end="" no print. 
O código a seguir, por exemplo, imprimirá o texto "abc":

print("a", end="")
print("d", end="")
print("c")

Dica 2: algumas alternativas para concatenar duas strings sem incluir um espaço:

print("a", "b", sep="") 
# especificando o parâmetro sep (é possível usar os parâmetros sep e end simultaneamente)
print("a" + "b")
print("a" + str(n)) 
# se n for um número, é necessário converter para str antes como indicado neste exemplo

Os seguintes testes serão realizados,  
ENTRADA 01:

10

SAIDAS 01:

0  1  2  3  4  5  6  7  8  9  10
10  9  8  7  6  5  4  3  2  1  0


ENTRADA 02:

5

SAIDAS 02:

0  1  2  3  4  5
5  4  3  2  1  0
'''

num = int(input())
count = 1
result = "0"

while count < num + 1:
  result += " " + str(count)
  count += 1

print(result)

count = 1
result = str(num)

while count < num + 1:
  result += " " + str(num - count)
  count += 1

print(result)