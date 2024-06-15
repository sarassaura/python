'''
Escreva um programa que leia uma matriz para armazenar as C notas 
de uma turma e calcular a média de cada um dos L alunos. Portanto, 
será lida uma matriz com L linhas (uma para cada aluno) e 
C colunas (cada coluna terá uma nota).

Para ler a matriz, primeiro será informado o número de linhas e 
depois o número de colunas. Após a leitura das dimensões da matriz, 
os elementos de cada linha da matriz estão dispostos linha por linha. 
Por exemplo (as duas primeiras linhas são as dimensões da matriz: 
número de linhas (2) e número de colunas(3)):

2
3
6 9 6
7 8 9

Após isso, calcule a média (aritmética) das C notas para cada aluno e 
adicione a coluna C+1 com a média. Após isso, imprima a matriz completa, 
com L linhas e C+1 colunas.

Dica (Python): exemplo de código para ler os elementos de uma matriz 
no formato descrito no enunciado:

n_linhas = int(input())
n_colunas = int(input())
matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
for linha in range(n_linhas):
    itens_linha = input().split(" ")
    for coluna in range(n_colunas):
        matriz[linha][coluna] = float(itens_linha[coluna])                

Dica (Java): exemplo de código para ler os elementos de uma matriz 
no formato descrito no enunciado:

Scanner leitor = new Scanner(System.in);
int n_linhas = leitor.nextInt();
int n_colunas = leitor.nextInt();
double[][] matriz = new double[n_linhas][n_colunas];
for (int linha = 0; linha < n_linhas; linha++)
    for (int coluna = 0; coluna < n_colunas; coluna++)
        matriz[linha][coluna] = leitor.nextDouble();

Entrada:

    L (número de alunos)
    C (quantidade de notas)
    Elementos da matriz

Exemplo:

2
3
6 9 6
7 8 9

Saída:

    Matriz com dimensões L x C+1

Observação: Imprima os valores da matriz com duas casas decimais.

Exemplo:

6.00 9.00 6.00 7.00
7.00 8.00 9.00 8.00

Fonte: Ex.1 (cap 6)  - livro texto 
(Neves, R.; Zampirolli, F. Processando a Informação. Editora UFABC, 2017).
'''

l = int(input())
c = int(input())

m = [[0 for i in range(c)] for j in range(l)]

for line in range(l):
    items = input().split(" ")
    for column in range(c):
        m[line][column] = float(items[column])

for x in range(l):
    median = 0
    for y in range(c):
        median += m[x][y]
    median /= c
    m[x].append(median)

for x in range(l):
    for y in range(c + 1):
        print("{:.2f}".format(m[x][y]), sep=' ', end=' ')
    print()
