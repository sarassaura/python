'''
Escreva um programa, usando estrutura de repetição while, 
para ler N valores e determinar o menor 
entre aqueles que estiverem dentro do intervalo fechado [a, b]. 
Seu programa deve primeiramente receber o valor N e 
os limites a e b, para só então ler os valores e 
efetuar o processamento requerido. 

Caso não haja valores dentro do intervalo, 
o programa deve emitir uma mensagem de erro do tipo: 
"Sem valores no intervalo definido.". 
Se houver valores, a saída do programa deve ser: 
"O menor valor no intervalo vale x.", 
em que x deve ter exatamente duas casas decimais. 

Dica: para encontrar o menor valor você pode inicializar 
a respectiva variável como float('inf') e 
atualizá-la conforme os valores forem apresentados. 

O float('inf') cria um número infinito e deve ser usado, por exemplo, da seguinte forma:

a = float('inf')
Neste caso, o valor de a será um número infinito.
'''

N = int(input())
A = int(input())
B = int(input())
menor = float('inf')

while N > 0:
    number = float(input())

    if number >= A and number <= B and number < menor:
        menor = number

    N -= 1

if menor == float('inf'):
    print("Sem valores no intervalo definido.")
else:
    print("O menor valor no intervalo vale {:.2f}.".format(menor))