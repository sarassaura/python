'''
Escreva um programa que leia um vetor de inteiros com n elementos. 
Depois verifique se o vetor está ordenado em ordem crescente.

Observação: após a leitura do valor n, os elementos do vetor 
estão todos dispostos em apenas uma linha. Por exemplo:

3
3 1 2


Dica (Python): para ler elementos em uma mesma linha, 
pode ser usado o método split após a leitura. 
Veja exemplo a seguir:

n = int(input())
v = [0] * n

itens_linha = input().split(" ")
for i in range(n):
    v[i] = int(itens_linha[i])

Dica (Java): exemplo de código para ler elementos em uma mesma linha.

Scanner leitor = new Scanner(System.in);
int n = leitor.nextInt();
int[] v = new int[n];
for (int i = 0; i < n; i++)
    v[i] = leitor.nextInt();

Entrada:

    Um valor n (0 <= n <= 50);

    n inteiros

Saída:

    Imprima "SIM" se o vetor estiver ordenado e "NAO" caso contrário
'''

n = int(input())
v = [0] * n
yes = True

itens_linha = input().split(" ")

for i in range(n):
    v[i] = int(itens_linha[i])

bef = v[0]

for x in range(1, n):
    if v[x] < bef:
        print("NAO")
        yes = False
        break
    bef = v[x]

if yes == True:
    print("SIM")