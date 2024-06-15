'''
Faça um programa que leia um valor inteiro N que representa a 
quantidade de linhas para impressão de uma pirâmide de números 1. 
A figura impressa é composta apenas pelos caracteres hífen (-) e o número 1. 
Por exemplo, uma pirâmide com altura 5 deve ser representada da seguinte forma:

----1----
---111---
--11111--
-1111111-
111111111


Dica (Python): é possível imprimir sem quebrar linha usando o parâmetro end do método print.
print("1", end="")

Dica (Java): é possível imprimir sem quebrar linha usando 
o método System.out.print() ao invés de System.out.println(). 
Veja nos exemplos a seguir (observação: apenas os comandos de 
impressão são mostrados na tabela, mas o programa em Java precisa 
incluir outros componentes, como declaração da classe, método main, etc).
System.out.print("1");

Entrada:

    Quantidade de linhas (altura) da pirâmide


Saída:

    Pirâmide
'''

n = int(input())
ones = "1"
hifens = ""

for y in range(n - 1):
    hifens += "-"

for x in range(n):
    print(hifens[x:] + ones + hifens[x:])
    ones += "11"