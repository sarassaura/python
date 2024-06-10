'''
Uma fábrica de discos voadores produz diversos modelos 
que são entregues para clientes na galáxia. Nesta fábrica, 
os discos voadores são vendidos em pacotes com três unidades. 
Portanto, não é possível comprar apenas um disco voador nesta fábrica. 
Ao solicitar os três discos voadores, devem ser especificados 
os modelos dos discos. Dependendo dos modelos solicitados, 
o prazo de entrega pode ser diferente:

    Quando os três discos voadores solicitados são do mesmo modelo 
    (tem o mesmo código), o prazo de entrega é de 5 dias;

    Quando dois discos voadores são do mesmo modelo (tem o mesmo código) 
    e o outro é de outro modelo (outro código), o prazo de entrega é de 15 dias;

    Quando os três discos voadores são de modelos diferentes 
    (três códigos diferentes), o prazo de entrega é de 30 dias.


O gerente da fábrica escreveu um programa para calcular o prazo de entrega 
dependendo dos modelos solicitados pelo cliente, mas faltou implementar a 
função/método para calcular o prazo de entrega:

Python:

def obter_prazo_entrega(disco1, disco2, disco3):
    #codigo da funcao aqui
    
d1 = int(input())
d2 = int(input())
d3 = int(input())
prazo_entrega = obter_prazo_entrega(d1, d2, d3)
print("Disco1 =", d1)
print("Disco2 =", d2)
print("Disco3 =", d3)
print("Prazo de entrega =", prazo_entrega)

Java:

import java.util.Scanner;

public class Programa {
    
    public static int obterPrazoEntrega(int disco1, int disco2, int disco3) {
        // Este método deve retornar o prazo de entrega
        
    }
    
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        int d1 = leitor.nextInt();
        int d2 = leitor.nextInt();
        int d3 = leitor.nextInt();
        int resultado = obterPrazoEntrega(d1, d2, d3);
        System.out.println("Disco1 = " + d1);
        System.out.println("Disco2 = " + d2);
        System.out.println("Disco3 = " + d3);
        System.out.println("Prazo de entrega = " + resultado);
    }
    
}

Escreva a função/método para obter o prazo de entrega. 
Essa função/método recebe os códigos de três discos voadores e deve retornar 
o prazo de entrega dependendo dos códigos dos discos voadores solicitados.


Python (o arquivo submetido deve ter a extensão .py):

def obter_prazo_entrega(disco1, disco2, disco3):
    #codigo da funcao

Java (o arquivo submetido deve ter a extensão .java):

public static int obterPrazoEntrega(int disco1, int disco2, int disco3) {
    // codigo do metodo
}

Entrada:

    Código do modelo do disco voador 1
    Código do modelo do disco voador 2
    Código do modelo do disco voador 3

Saída:

    Códigos dos modelos dos discos voadores
    Valor retornado pela função/método
'''

def obter_prazo_entrega(disco1, disco2, disco3):
    if disco1 == disco2 == disco3:
        return 5
    elif disco1 != disco2 and disco2 != disco3 and disco3 != disco1:
        return 30
    else:
        return 15